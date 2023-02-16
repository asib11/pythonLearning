from csv import DictWriter

with open('dict_writer.csv', 'w') as file:
    header = ['name', 'id', 'intake']
    writer = DictWriter(file, fieldnames= header)
    writer.writeheader()
    writer.writerow({'name': 'asib', 'id': 31, 'intake': 40})