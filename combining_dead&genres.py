import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

# Figure out which artists have no genre
# Make set with all dead musicians 
all_dead = set() 
with open('alldeadmusicians.csv', encoding='utf-8') as file:
    file.readline()
    for line in file:
        all_dead.add(line.split(';')[0].split('(')[0].strip())
print(len(all_dead))        

# Make set of dead musicians who do have a genre
dead_with_genre = set() 
with open('death_genre.csv', encoding='utf-8') as file:
    file.readline()
    for line in file:
        dead_with_genre.add(line.split(';')[0].split('(')[0].strip())
print(len(dead_with_genre))  

# Subtract musicians with genre from all musicians to get musicians without genre  
dead_without_genre = all_dead.difference(dead_with_genre)
print(len(dead_without_genre))

with open('dead_musicians_with_genre_from_spotify.csv', 'w', encoding='utf-8') as file:
    file.write('label;genre\n')
    for name in dead_without_genre:
        results = spotify.search(q='artist:' + name, type='artist')
        items = results['artists']['items']
        if len(items) > 0:
            artist = items[0]
            file.write(f"{name};{artist['genres']}\n")

with open('dead_musicians_with_genre_from_spotify.csv', encoding='utf-8') as input_file:
    with open('correct_dead_musicians_with_genre_from_spotify.csv', 'w', encoding='utf-8') as output_file:
        input_file.readline()
        for line in input_file:
            if line.split(';')[-1].strip() != '[]':
                output_file.write(line)

# Combine the two datasets with genre
dead_genre_set2 = set() 
with open('correct_dead_musicians_with_genre_from_spotify.csv', encoding='utf-8') as file:
    file.readline()
    for line in file:
        dead_genre_set2.add(line.split(';')[0].split('(')[0].strip())
print(len(dead_genre_set2))         

dead_without_genre = dead_genre_set2.add(dead_with_genre)
print(len(dead_without_genre))

