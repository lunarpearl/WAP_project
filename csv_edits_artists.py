with open ('artists.csv', encoding='utf8') as input_file:
    with open('artist_id.csv','w') as output_file:
        for line in input_file:
            output_file.write(';'.join(line.split(',')[:3])+'\n')
