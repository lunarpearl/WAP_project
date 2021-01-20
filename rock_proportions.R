library(tidyverse)

allmusicians_genre <- read_csv2('allmusic_genre.csv')
#making a subset that only includes all musicians that have 'rock' in their genres
allrock <- allmusicians_genre[grep('rock',allmusicians_genre$genre), ignore.case = TRUE]
#calculate number of rock musicians within all musicians
number_allmusicians <- nrow(allmusicians_genre)
number_rock <- nrow(allrock)
proportion_rock_inall <- number_rock/number_allmusicians
#now we look at only musicians that passed away
deadmusicians_genre <- read_csv2('death_genre.csv')
#subset of dead rock musicians
deadrock <- deadmusicians_genre[grep('rock',deadmusicians_genre$genre,ignore.case = TRUE), ]
#calculate number of rock musicians that passed away
number_deadmusicians <- nrow(deadmusicians_genre)
number_deadrock <- nrow(deadrock)
proportion_rock_indead <- number_deadrock/number_deadmusicians
#create a data frame and dump proportions in there
percentages <- data.frame(proportion_rock_inall,proportion_rock_indead)
percentages <- as.data.frame(t(percentages))
percentages <- percentages %>% rename(percentage = V1) %>% tibble::rownames_to_column('sample')
#create a barplot for the proportions expressed as percentages
ggplot(data = percentages)+aes(x=sample,y=percentage)+geom_col(fill='steelblue')+labs(title = 'Percentages of rock stars within all musicians and within passed away musicians.')+xlab(NULL)+ylab(NULL)+scale_y_continuous(labels = scales::label_percent(accuracy = 1L))+theme_minimal(base_size = 10)+geom_text(aes(label=scales::percent(percentage)),vjust=1.6,colour='white')+scale_x_discrete(labels=c('Within all musicians','Within passed away'))