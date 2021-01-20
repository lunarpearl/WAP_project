artist_id_to_name = {}

# Link id to artists name
with open('artist_id.csv') as id_file:
    id_file.readline()
    for row in id_file:
        id_, real_name, art_name = row.split(';')
        artist_id_to_name[id_] = real_name   # include art_name later

# Read in other file & replace id in other file with corresponding artist name
with open('artist_genre.csv') as genre_file:
    with open('artist&genre.csv', 'w') as combined_file:
        genre_file.readline()
        for line in genre_file:
            artist_id, genre = line.split(';')
            combined_file.write(f'{artist_id_to_name[artist_id]};{genre}')





