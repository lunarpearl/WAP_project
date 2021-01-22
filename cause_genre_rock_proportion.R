library(tidyverse)
#loading csv with only those artists that have cause of death & genre matched from spotify
cause_genre <- read_csv2('from_all_causes_of_death_with_genre_from_spotify.csv')
#subgroup with rock genre
rock <- cause_genre[grep('rock',cause_genre$genre,ignore.case = TRUE), ]
#proportion
rock_proportion_in_cause <- nrow(rock)/nrow(cause_genre)*100