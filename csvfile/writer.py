from csv import reader, writer

with open('reader.csv') as file:
    read_file = reader(file)
    with open('writer.csv', 'w') as file:
        write_file = writer(file)
        for row in read_file:
            write_file.writerow([i.upper() for i in row])