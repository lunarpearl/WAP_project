
library(tidyverse)

## Load in csv as dataframe
df <- read_csv2('death_genre.csv')

## Transform birth and death dates to date formats 
## + calculate age at death
## + add logical expression column if the genre contains rock or not
calculations_df <- df %>%
  mutate(`birth date` = as.Date(`birth date`),
         `death date` = as.Date(`death date`),
         days_at_death = `death date` - `birth date`,
         age_at_death = days_at_death / 365.25,
         is_rock = str_detect(genre,coll("rock", ignore_case = TRUE)))

clean_df <- subset(calculations_df, !(age_at_death <= 17)) %>%
  mutate(age_at_death = as.numeric(age_at_death))

## Group by the logical expression then calculate count, mean age, SD of age
summary_df <- clean_df %>%
  select(age_at_death, is_rock) %>%
  group_by(is_rock) %>%
  summarise(n = n(),
            m_age_at_death = mean(age_at_death),
            SD = sd(age_at_death),
            statistic = shapiro.test(age_at_death)$statistic,
            p.value = shapiro.test(age_at_death)$p.value,
            median = median(age_at_death),
            IQR = IQR(age_at_death))
#Shapiro-Wilks test of normality is singificant, assumption of normality is not met


# Boxplot visualization
# install.packages("ggpubr")
library(ggpubr)
ggboxplot(clean_df, x = "is_rock", y = "age_at_death", 
          color = "is_rock", 
          ylab = "Age at death", xlab = "Genre of artist", ) +
  scale_x_discrete(labels = c("Other", "Rock")) +
  scale_color_discrete(labels = c("Other", "Rock"), name="Genre")
#palette = c("#00AFBB", "#E7B800")

## Histogram
ggplot(clean_df, aes(x = age_at_death, fill = is_rock)) +
  geom_histogram(position = "identity", bins = 30, alpha=0.5) +
  labs(x = "Age at Death", y = "Count", fill = "Genre of artist",
       title = "Histogram",
       subtitle = ) +
  scale_fill_discrete(labels = c("Other", "Rock"))


#lines(seq(10, 40, by=.5), dnorm(seq(10, 40, by=.5),
                               # mean(mtcars$mpg), sd(mtcars$mpg)), col="blue")

# Normalized histogram visualization
ggplot(clean_df, aes(x = age_at_death, fill = is_rock)) +
  geom_histogram(aes(y = 2*(..density..)/sum(..density..)),
                 position = "identity", bins = 30, alpha=0.5) +
  labs(x = "Age at Death", y = "Count per Group Count", fill = "Genre of artist",
       title = "Normalized Histogram",
       subtitle = ) +
  scale_fill_discrete(labels = c("Other", "Rock"))


## Q-Q plots
ggqqplot(clean_df, x = "age_at_death", facet.by = "is_rock")

library(car)
## Levene's test with one independent variable
# leveneTest(age_at_death ~ is_rock, data = clean_df) #p = 0.0099 not met

## Independent t-test - only if we were able to assume equal distribution, but no
# t.test (age_at_death ~ is_rock, var.equal=FALSE, data = clean_df)

## Wilcoxon test - since assumption of normality is not met
wilcox.test(age_at_death ~ is_rock, data = clean_df)

## Get effect size
library(rstatix)
clean_df %>% wilcox_effsize(age_at_death ~ is_rock)
clean_df %>%
  group_by(is_rock) %>%
  get_summary_stats(age_at_death, type = "median_iqr")
