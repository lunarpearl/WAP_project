from os import remove
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

# Figure out which artists have no genre
# Make set with all dead musicians 
causes_of_death = set() 
with open('music.csv', encoding='utf-8') as file:
    file.readline()
    for line in file:
        causes_of_death.add(line.split(';')[0].split('(')[0].strip())
print(len(causes_of_death))        

with open('cause_of_death_with_genre_from_spotify.csv', 'w', encoding='utf-8') as file:
    file.write('label;genre\n')
    for name in causes_of_death:
        results = spotify.search(q='artist:' + name, type='artist')
        items = results['artists']['items']
        if len(items) > 0:
            artist = items[0]
            file.write(f"{name};{artist['genres']}\n")

with open('cause_of_death_with_genre_from_spotify.csv', encoding='utf-8') as input_file:
    with open('correct_cause_of_death_with_genre_from_spotify.csv', 'w', encoding='utf-8') as output_file:
        input_file.readline()
        for line in input_file:
            if line.split(';')[-1].strip() != '[]':
                output_file.write(line)
