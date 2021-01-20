
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
            p.value = shapiro.test(age_at_death)$p.value)


# Boxplot visualization
# install.packages("ggpubr")
library(ggpubr)
ggboxplot(clean_df, x = "is_rock", y = "age_at_death", 
          color = "is_rock", palette = c("#00AFBB", "#E7B800"),
          ylab = "Age at death", xlab = "Groups")

#Histogram visualization
ggplot(clean_df, aes(x = age_at_death)) +
  geom_histogram(aes(color = is_rock), fill = "white",
                 position = "identity", bins = 30) +
  scale_color_manual(values = c("#00AFBB", "#E7B800"))

## Q-Q plots
ggqqplot(clean_df, x = "age_at_death", facet.by = "is_rock")

library(car)
# Levene's test with one independent variable
leveneTest(age_at_death ~ is_rock, data = clean_df) #p = 0.0099 not met

## Independent t-test
t.test (age_at_death ~ is_rock, var.equal=FALSE, data = clean_df)



