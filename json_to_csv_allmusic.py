import json

with open ('genre_all_musicians.json', encoding='utf-16') as file:
    genre_all = json.load(file)

# List of directory with only title and description as keys
genre_dict = []
for dict in genre_all:
    x = {'genre':dict.get('ontology/genre_label'), 'label':dict.get('http://www.w3.org/2000/01/rdf-schema#label')}
    genre_dict.append(x)

## Creating csv file
with open('allmusic_genre.csv', 'w', encoding="utf-8") as file:
    file.write("label;genre\n")
    for person in genre_dict:
        file.write(f"{person['label']};{person['genre']}\n")