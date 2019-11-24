from reader import reader_csv

#Creating list to periodic table
list_periodic_table = list()

#Turning object in list
reader = reader_csv()
for line in reader:
    list_periodic_table.append(line)

#Analizing answer
def get_option(n_answer):
    if n_answer == 1:
        nAtomic = int(input("Número Atômico: "))
        print_result(nAtomic)
        input("Aperte Enter para voltar...\n\n")
        print("\x1b[2J")
    elif n_answer == 2:
        nameElement = str(input("Nome do Elemento: "))
        nAtomic = return_position(removeCharacteresEspeciais(nameElement.lower()))
        print_result(nAtomic)
        input("Aperte Enter para voltar...\n\n")
        print("\x1b[2J")
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
    
def print_result(value):
    print(f"""
          
    Número Atômico: {list_periodic_table[value - 1][0]}
    Nome do Elemento: {list_periodic_table[value - 1][1]}
    Símbolo: {list_periodic_table[value - 1][2]}
    Massa Atômica: {list_periodic_table[value - 1][3]}
    Estado Físico Natural: {list_periodic_table[value - 1][4]}
    Distribuição Eletrônica: {list_periodic_table[value - 1][5]}
    """)

# Return position of name of element
def return_position(string_name_element):
    names_elements = []
    for i in range(0, len(list_periodic_table)):
        names_elements.append(removeCharacteresEspeciais(list_periodic_table[i][1].lower()))
    position_element = names_elements.index(string_name_element)
    return position_element + 1

#Metod to remove characteres especiais of text
def removeCharacteresEspeciais(text):
    from unicodedata import normalize
    return normalize('NFKD', text).encode('ASCII','ignore').decode('ASCII')






