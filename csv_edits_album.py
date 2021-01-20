import csv

with open ('albums.csv') as file:
    reader = csv.reader(file)
    with open('artist_genre.csv','w') as result:
        writer= csv.writer(result)
        for r in reader:
            writer.writerow((r[1], r[3]))
            

# # List of directory with only title and description as keys
# genre_dict = []
# for dict in genres:
#     x = {'genre':dict.get('ontology/genre_label'), 'label':dict.get('http://www.w3.org/2000/01/rdf-schema#label')}
#     genre_dict.append(x)

# ## Creating csv file
# with open('artist_genre.csv', 'w', encoding="utf-8") as file:
#     file.write("artist;genre\n")
#     for person in genres:
#         file.write(f"{person['artist']};{person['genre']}\n")