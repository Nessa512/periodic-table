import csv

def reader_csv():
    csv_file = open("tabela.csv", "r")
    reader = csv.reader(csv_file)
    next(reader)
    return reader
    