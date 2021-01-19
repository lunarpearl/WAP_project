import json

## Open large set of people with death causes
with open('deathcause.json', encoding='utf-16') as file:
    data = json.load(file)

## Defining list with keywords
keywords = ['singer', 'songwriter', 'music', 'discography', 'violinist', 'band', 'guitarist', 'drummer']

## Reduce data to only those who have 'music' in their description
reduced_data = []
for dict in data:
    for key in keywords:
        if 'http://purl.org/dc/elements/1.1/description' in dict and key in str(dict["http://purl.org/dc/elements/1.1/description"]).lower() and dict not in reduced_data:
            reduced_data.append(dict.copy()) 

## Creating subset json file 
with open('reduced_dataset.json', 'w') as file:
    json.dump(reduced_data, file, indent=1)

## List of directory with only title and description as keys
music_dict = []
for dict in reduced_data:
    x = {'title':dict['title'] ,'description':dict['http://purl.org/dc/elements/1.1/description'],'cause of death':dict['ontology/deathCause_label']}
    music_dict.append(x)

## Creating csv file
with open('music.csv', 'w', encoding="utf-8") as file:
    file.write("title,description,cause of death\n")
    for person in music_dict:
        file.write(f"{person['title']},{person['description']},{person['cause of death']}\n")
