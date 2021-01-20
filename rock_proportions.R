library(tidyverse)

allmusicians_genre <- read_csv2('allmusic_genre.csv')
#making a subset that only includes all musicians that have 'rock' in their genres
allrock <- allmusicians_genre[grep('rock',allmusicians_genre$genre), ignore.case = TRUE]
#calculate number of rock musicians within all musicians
number_allmusicians <- nrow(allmusicians_genre)
number_rock <- nrow(allrock)
proportion_rock_inall <- number_rock/number_allmusicians*100
#now we look at only musicians that passed away
deadmusicians_genre <- read_csv2('death_genre.csv')
#subset of dead rock musicians
deadrock <- deadmusicians_genre[grep('rock',deadmusicians_genre$genre,ignore.case = TRUE), ]
#calculate number of rock musicians that passed away
number_deadmusicians <- nrow(deadmusicians_genre)
number_deadrock <- nrow(deadrock)
proportion_rock_indead <- number_deadrock/number_deadmusicians*100