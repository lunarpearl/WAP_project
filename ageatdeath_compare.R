
library(tidyverse)

df <- read_csv2('death_genre.csv')

calculations_df <- df %>%
  mutate(`birth date` = as.Date(`birth date`),
         `death date` = as.Date(`death date`),
         days_at_death = `death date` - `birth date`,
         age_at_death = days_at_death / 365.25,
         is_rock = str_detect(genre,coll("rock", ignore_case = TRUE)))

summary_df <- drop_na(calculations_df) %>%
  select(age_at_death, is_rock) %>%
  group_by(is_rock) %>%
  summarise(m_age_at_death = mean(age_at_death))

