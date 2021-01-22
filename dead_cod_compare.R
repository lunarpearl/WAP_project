library(tidyverse)
df_cod <- read_csv2('music.csv')
df_dead <- read_csv2('alldeadmusicians.csv')

## Cleaning up and calculateing age at death for both groups
df_cod_clean <- df_cod %>%
  select("birth date", "death date", "cause of death") %>%
  mutate(`cause of death` = TRUE,
         `birth date` = as.Date(`birth date`),
         `death date` = as.Date(`death date`),
         days_at_death = `death date` - `birth date`,
         age_at_death = days_at_death / 365.25) %>%
  drop_na()

df_dead_clean <- df_dead %>%
  select("birth date", "death date") %>%
  mutate(`birth date` = as.Date(`birth date`),
         `death date` = as.Date(`death date`),
         `cause of death` = FALSE,
         days_at_death = `death date` - `birth date`,
         age_at_death = days_at_death / 365.25) %>%
  drop_na()

## Combining the two dataframes
total_df <- rbind(df_dead_clean, df_cod_clean)
clean_df <- subset(total_df, !(age_at_death <= 17))

## Creating the summary table
summary_df <- clean_df %>%
  group_by(`cause of death`) %>%
  summarise(n = n(),
            m_age_at_death = mean(age_at_death),
            SD = sd(age_at_death),
            median = median(age_at_death),
            IQR = IQR(age_at_death))

## Normalized histogram
ggplot(clean_df, aes(x = age_at_death, y = 2*(..density..)/sum(..density..),
                     fill = `cause of death`)) +
  geom_histogram(position = "identity", bins = 30, alpha=0.5) +
  labs(x = "Age at Death", y = "Normalized Frequency", fill = NULL,
       title = NULL) +
  scale_fill_discrete(labels = c("All", "Recorded COD"))
