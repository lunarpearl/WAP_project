import json

with open('deathcause.json', encoding='utf-16') as alldeathcauses_file:
    all_deathcauses = json.load(alldeathcauses_file)

# with open('artist&genre.csv') as combi_file:
#     for line in combi_file:
#         real_name, art_name, genre = line.strip().split(';')

genre_dict = []
for dict in all_deathcauses:
    x = {'birth date':dict.get('ontology/birthDate'), 'genre':dict.get('ontology/genre_label'), 'death date':dict.get('ontology/deathDate'), 'label':dict.get('http://www.w3.org/2000/01/rdf-schema#label')}
    genre_dict.append(x)

# Match the information from artist&genre with the dead_musicians file to find genres for artists from whom the genre was not noted yet.
# Output should be at least 5,600 rows, of name and genre
# with open('musicians_with_death_causes.csv', 'w', encoding='utf-8') as deadgenre_file:  # Expanded data set
    with open('artist&genre.csv') as combi_file:
        for line in combi_file: 
            real_name, art_name, genre = line.strip().split(';')  
            # Look through the dead_musicians file whether the label matches up with
            # the real name or stage name in the artist&genre file
            # deadgenre_file.write("label;birth date;death date;genre\n")
            for person in all_deathcauses:
                if person.get('http://www.w3.org/2000/01/rdf-schema#label') in [real_name, art_name]:
                    print(person)
                    # deadgenre_file.write(f"{person['label']};{person['birth date']};{person['death date']};{person['genre']}\n")