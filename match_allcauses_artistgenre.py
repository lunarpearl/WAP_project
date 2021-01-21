import json
#change underscores to spaces to be able to compare names

with open('artist&cause&genre.csv','r+', encoding='utf-8') as matched_file:
    with open('deathcause.json',encoding='utf-16') as json_file:
        cause_source = json.load(json_file)
        for line in cause_source:
            line['title']=str(line['title']).replace('_',' ')
        with open('artist&genre.csv') as genre_source:
            genre_source.readline()
            for artist in genre_source:
                real_name, art_name, genre = artist.strip().split(';')
                for line in cause_source:
                    if 'ontology/deathCause_label' in line:
                        if real_name in line['title'] or art_name in line['title']:
                            matched_file.write(f'{real_name};{genre};{line["ontology/deathCause_label"]}\n')
                        if 'ontology/birthName' in line and real_name in line['ontology/birthName'] and real_name not in matched_file:
                            matched_file.write(f'{real_name};{genre};{line["ontology/deathCause_label"]}\n')

