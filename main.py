import csv

with open('tabela.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for nAtomico, nome, simbolo, mAtomica, estadoFisico, configEletronica in reader:
        print("""
    Número atômico: {}
    Nome do elemento: {}
    Simbolo do elemento: {}
    Massa atômica: {}
    Estado físico: {}
    Distribuição eletrônica: {}
    """.format(nAtomico,
               nome,
               simbolo,
               mAtomica,
               estadoFisico,
               configEletronica))
