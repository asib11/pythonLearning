from csv import DictReader

with open('reader.csv') as file:
    dic_read = DictReader(file, delimiter=',')
    for row in dic_read:
        print(row)
#DicReader speciality is it can read separate the value by header as key