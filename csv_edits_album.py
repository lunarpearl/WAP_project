with open ('albums.csv', encoding='utf8') as input_file:
    with open('artist_genre.csv','w') as output_file:
        for line in input_file:
            artist_id = line.split(',')[1]
            genre = line.split(',')[3]
            output_file.write(f'{artist_id};{genre}\n')