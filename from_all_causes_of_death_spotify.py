import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

# Convert the file from json to csv
with open ('deathcause.json', encoding='utf-16') as file:
    cause_of_death = json.load(file)

# List of directory with only label, cause of death, adn genre as keys
genre_dict = []
for dict in cause_of_death:
    x = {'genre':dict.get('ontology/genre_label'), 'cause of death':dict['ontology/deathCause_label'], 'label':dict.get('http://www.w3.org/2000/01/rdf-schema#label')}
    genre_dict.append(x)

## Creating csv file
with open('causes_of_death.csv', 'w', encoding="utf-8") as file:
    file.write("label;genre;cause of death\n")
    for person in genre_dict:
        file.write(f"{person['label']};{person['genre']};{person['cause of death']}\n")

# Make a dictionary of the csv file 
causes_of_death = {}
with open('causes_of_death.csv', encoding='utf-8') as file:
    file.readline()
    for line in file:
        columns = line.split(';')
        causes_of_death[(columns[0].split('(')[0].strip())] = columns[2].strip()
print(len(causes_of_death))        

# Run the names from the dictionary through the spotify API, add genres for all matches and write to a file
with open('from_all_causes_of_death_with_genre_from_spotify.csv', 'w', encoding='utf-8') as file:
    file.write('label;genre;cause of death\n')
    for name, cause in causes_of_death.items():
        results = spotify.search(q='artist:' + name, type='artist')
        items = results['artists']['items']
        if len(items) > 0:
            artist = items[0]
            if name == artist['name']:
                if len(artist['genres']) > 0:
                    file.write(f"{name};{artist['genres']};{cause}\n")
