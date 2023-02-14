from csv import reader

with open('reader.csv') as file:
    read_file = reader(file)
    next(read_file) # if want to show without header
    for row in read_file:
        print(row)

#whole data convert in a list 
# with open('reader.csv') as file:
#     read_file = list(reader(file))
#     print(read_file[0]) 