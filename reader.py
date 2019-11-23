import csv

def reader_csv():
    csv_file = open("./data/table.csv", "r")
    reader = csv.reader(csv_file)
    next(reader)
    return reader
    