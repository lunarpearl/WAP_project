import json

with open('deathcause.json', encoding='utf-16') as file:
    data = json.load(file)

reduced_data = []
for dict in data:
    if 'http://purl.org/dc/elements/1.1/description' in dict and 'music' in str(dict["http://purl.org/dc/elements/1.1/description"]).lower():
        reduced_data.append(dict.copy()) 


with open('reduced_dataset.json', 'w') as file:
    json.dump(reduced_data, file, indent=1)
