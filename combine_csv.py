artist_id_to_name = {}
artist_id_to_genres = {}

# Link id to artists name
with open('artist_id.csv') as id_file:
    id_file.readline()
    for row in id_file:
        id_, real_name, art_name = row.split(';')
        artist_id_to_name[id_] = real_name   # include art_name later

# Dictionary that link artist id's to list of genres
# Loop over artist_id file with output file 
# For each of the artists fill in list of genres together with artist name

with open('artist_genre.csv') as genre_file:
    genre_file.readline()
    for line in genre_file:
        artist_id, genre = line.split(';')
        if artist_id in artist_id_to_genres:
            artist_id_to_genres[artist_id].append(genre.strip())
        else:
            artist_id_to_genres[artist_id] = [genre.strip()] 

with open('artist&genre.csv', 'w') as combined_file:
     with open('artist_id.csv') as id_file:
        id_file.readline()
        for row in id_file:
            artist_id, real_name, art_name = row.strip().split(';')
            if artist_id in artist_id_to_genres:
                combined_file.write(f'{real_name};{art_name};{artist_id_to_genres[artist_id]}\n')

# 86% of artists has a genre
