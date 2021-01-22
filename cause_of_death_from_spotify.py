import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

# Make a dictionary of the csv file 
causes_of_death = {}
with open('music.csv', encoding='utf-8') as file:
    file.readline()
    for line in file:
        columns = line.split(';')
        causes_of_death[(columns[0].split('(')[0].strip())] = columns[6].strip()
print(len(causes_of_death))   

# Run the names from the dictionary through the spotify API, add genres for all matches and write to a file
with open('cause_of_death_with_genre_from_spotify.csv', 'w', encoding='utf-8') as file:
    file.write('label;genre;cause of death\n')
    for name, cause in causes_of_death.items():
        results = spotify.search(q='artist:' + name, type='artist')
        items = results['artists']['items']
        if len(items) > 0:
            artist = items[0]
            if len(artist['genres']) > 0:
                file.write(f"{name};{artist['genres']};{cause}\n")

