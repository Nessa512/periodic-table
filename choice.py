from reader import reader_csv

#Creating list to periodic table
list_periodic_table = list()

#Turning object in list
reader = reader_csv()
for line in reader:
    list_periodic_table.append(line)
"""
elements = []
symbols = []
atomic_weights = []
phases = []
electron_configs = [] 
"""

#Analizing answer
def get_option(n_answer):
    if n_answer == 1:
        option1()
    elif n_answer == 2:
        pass
    elif n_answer == 3:
        pass
    elif n_answer == 4:
        pass
    elif n_answer == 5:
        pass
    elif n_answer == 6:
        pass
    elif n_answer == 0:
        pass
    
def option1():
    nAtomic = int(input("Número Atômico: "))
    print_result(nAtomic)

def print_result(value):
    print(f"""
    Número Atômico: {list_periodic_table[value - 1][0]}
    Nome do Elemento: {list_periodic_table[value - 1][1]}
    Símbolo: {list_periodic_table[value - 1][2]}
    Massa Atômica: {list_periodic_table[value - 1][3]}
    Estado Físico: {list_periodic_table[value - 1][4]}
    Distribuição Eletrônica: {list_periodic_table[value - 1][5]}
    """)










