import json

with open ('genre_dead_musicians.json', encoding='utf-16') as file:
    genre_dead = json.load(file)

# List of directory with only label, birth date, death date, genre as keys
genre_dict = []
for dict in genre_dead:
    x = {'birth date':dict.get('ontology/birthDate'), 'genre':dict.get('ontology/genre_label'), 'death date':dict.get('ontology/deathDate'), 'label':dict.get('http://www.w3.org/2000/01/rdf-schema#label')}
    genre_dict.append(x)

# If the date of death/birth is a lsit, now it will only display the last one
for dict in genre_dict:
    if type(dict['birth date']) is list:
        del dict['birth date'][1]
        dict['birth date']=str(dict['birth date']).strip("['']")
    if type(dict['death date']) is list:
        del dict['death date'][1]
        dict['death date']=str(dict['death date']).strip("['']")

## Creating csv file
with open('death_genre.csv', 'w', encoding="utf-8") as file:
    file.write("label;birth date;death date;genre\n")
    for person in genre_dict:
        file.write(f"{person['label']};{person['birth date']};{person['death date']};{person['genre']}\n")
