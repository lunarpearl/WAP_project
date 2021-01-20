import csv

with open ('artists.csv', encoding='utf8') as file:
    reader = csv.reader(file)
    with open('artist_id.csv','w') as result:
        writer= csv.writer(result)
        for r in reader:
            writer.writerow((r[0], r[1], r[2]))
