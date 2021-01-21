import json

with open ('dead_musicians.json', encoding='utf-16') as file:
    genre_dead = json.load(file)

# List of directory with only title and description as keys
genre_dict = []
for dict in genre_dead:
    x = {'birth date':dict.get('ontology/birthDate'), 'death date':dict.get('ontology/deathDate'), 'label':dict.get('http://www.w3.org/2000/01/rdf-schema#label')}
    genre_dict.append(x)

## Creating csv file
with open('alldeadmusicians.csv', 'w', encoding="utf-8") as file:
    file.write("label;birth date;death date\n")
    for person in genre_dict:
        file.write(f"{person['label']};{person['birth date']};{person['death date']}\n")