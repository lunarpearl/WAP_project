import json

with open('dead_musicians.json', encoding='utf-16') as alldead_file:
    dead_musicians = json.load(alldead_file)

# with open('artist&genre.csv') as combi_file:
#     for line in combi_file:
#         real_name, art_name, genre = line.strip().split(';')

genre_dict = []
for dict in dead_musicians:
    x = {'birth date':dict.get('ontology/birthDate'), 'genre':dict.get('ontology/genre_label'), 'death date':dict.get('ontology/deathDate'), 'label':dict.get('http://www.w3.org/2000/01/rdf-schema#label')}
    genre_dict.append(x)

# Match the information from artist&genre with the dead_musicians file to find genres for artists from whom the genre was not noted yet.
# Output should be at least 5,600 rows, of name and genre
with open('more_deadpeople&genres.csv', 'w', encoding='utf-8') as deadgenre_file:  # Expanded data set
    with open('artist&genre.csv') as combi_file:
        for line in combi_file: 
            real_name, art_name, genre = line.strip().split(';')  
            # Look through the dead_musicians file whether the label matches up with
            # the real name or stage name in the artist&genre file
            deadgenre_file.write("label;birth date;death date;genre\n")
            for person in dead_musicians:
                if person.get('http://www.w3.org/2000/01/rdf-schema#label') in [real_name, art_name]:
                    deadgenre_file.write(f"{person['label']};{person['birth date']};{person['death date']};{person['genre']}\n")

# Expand the death_genre data set with dead musicians from the dead_musicians who do not have a genre yet
# We have a 43,000 names dataset of artists with genre (artist&genre)
# Run the names from dead_musicians through the artist&genre dataset and look for matches 
# For all matches add the name to the death_genre data set if they are not in there yet