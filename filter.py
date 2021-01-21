import json

## Open large set of people with death causes
with open('deathcause.json', encoding='utf-16') as file:
    data = json.load(file)

## Defining list with keywords
keywords = ['singer', 'singing', 'songwriter', 'music', 'discography', 'violinist', 'bandleader', 'guitarist', 'drummer']

## Reduce data to only those who have the above keywords in their description
reduced_data = []
for dict in data:
    for key in keywords:
        if 'http://purl.org/dc/elements/1.1/description' in dict and key in str(dict["http://purl.org/dc/elements/1.1/description"]).lower() and dict not in reduced_data:
            reduced_data.append(dict.copy()) 
        if 'ontology/occupation_label' in dict and key in str(dict["ontology/occupation_label"]).lower() and dict not in reduced_data:
            reduced_data.append(dict.copy()) 
        if 'ontology/occupation' in dict and key in str(dict["ontology/occupation"]).lower() and dict not in reduced_data:
            reduced_data.append(dict.copy()) 
        if 'http://www.w3.org/2000/01/rdf-schema#seeAlso_label' in dict and key in str(dict["http://www.w3.org/2000/01/rdf-schema#seeAlso_label"]).lower() and dict not in reduced_data:
            reduced_data.append(dict.copy())
#band is filtered separately, as otherwise it will include people who's occupation in a 'bandit'
    if 'ontology/knownFor' in dict and 'band' in str(dict["ontology/knownFor"]).lower() and dict not in reduced_data:
        reduced_data.append(dict.copy())
    if 'ontology/associatedMusicalArtist' in dict and 'band' in str(dict["ontology/associatedMusicalArtist"]).lower() and dict not in reduced_data:
        reduced_data.append(dict.copy())
    if 'ontology/associatedBand' in dict and 'band' in str(dict["ontology/associatedBand"]).lower() and dict not in reduced_data:
        reduced_data.append(dict.copy())


## Creating subset json file 
with open('reduced_dataset.json', 'w') as file:
    json.dump(reduced_data, file, indent=1)

## List of directory with the coloumns we want as keys
music_dict = []
for dict in reduced_data:
    x = {'title':dict['title'] ,'description':dict.get('http://purl.org/dc/elements/1.1/description'),'occupation':dict.get('ontology/occupation_label'),'birth date':dict.get('ontology/birthDate'), 'death date':dict.get('ontology/deathDate'),'cause of death':dict['ontology/deathCause_label']}
    music_dict.append(x)

## Creating csv file
with open('music.csv', 'w', encoding="utf-8") as file:
    file.write("title;description;occupation;birth date;death date;cause of death\n")
    for person in music_dict:
        file.write(f"{person['title']};{person['description']};{person['occupation']};{person['birth date']};{person['death date']};{person['cause of death']}\n")
