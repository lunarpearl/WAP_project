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
  mutate(age_at_death = as.numeric(age_at_death),
         year_of_death = format(as.Date(`death date`, format="%d/%m/%Y"),"%Y"),
         year_of_birth = format(as.Date(`birth date`, format="%d/%m/%Y"),"%Y"))

clean_df_modern <- subset(clean_df, !(year_of_birth < 1900))
summary_df_modern <- clean_df_modern %>%
  select(age_at_death, is_rock) %>%
  group_by(is_rock) %>%
  summarise(n = n(),
            m_age_at_death = mean(age_at_death),
            SD = sd(age_at_death),
            median = median(age_at_death),
            IQR = IQR(age_at_death))

history_df <- clean_df_modern %>%
  group_by(is_rock, year_of_death) %>%
  summarise(median_age = median(age_at_death),
            count = n()) %>%
  mutate(year_of_death = as.numeric(year_of_death))
  
## Group by the logical expression then calculate count, mean age, SD of age
summary_df <- clean_df %>%
  select(age_at_death, is_rock) %>%
  group_by(is_rock) %>%
  summarise(n = n(),
            m_age_at_death = mean(age_at_death),
            SD = sd(age_at_death),
            median = median(age_at_death),
            IQR = IQR(age_at_death))

# Normalized histogram visualization
ggplot(clean_df_modern, aes(x = age_at_death, fill = is_rock)) +
  geom_histogram(aes(y = 2*(..density..)/sum(..density..)),
                 position = "identity", bins = 30, alpha=0.5) +
  labs(x = "Age at Death", y = "Normalized Frequency", fill = "Genre",
       title = NULL) +
  scale_fill_discrete(labels = c("Other", "Rock"))

## Line graph of median age over time
ggplot(history_df) +
  aes(x = year_of_death, y = median_age, colour = is_rock) +
  geom_line() +
  geom_smooth() +
  labs(x = "Year of Death", y = "Median Age at Death", color = "Genre",
      title = NULL) +
  #scale_x_continuous(limits=c(2008, 2019), breaks = seq(2008, 2019, 2)) +
  xlim(1930, 2016) +
  ylim(20, 85) +
  scale_color_discrete(labels = c("Other", "Rock")) +
  scale_x_continuous(breaks = c(1930,1950,1970,1990,2010))

## Q-Q plots
# ggqqplot(clean_df_modern, x = "age_at_death", facet.by = "is_rock")


## Wilcoxon test - since assumption of normality is not met
wilcox.test(age_at_death ~ is_rock, data = clean_df_modern)
## Get effect size
library(rstatix)
clean_df_modern %>% wilcox_effsize(age_at_death ~ is_rock)
clean_df %>%
  group_by(is_rock) %>%
  get_summary_stats(age_at_death, type = "median_iqr")
