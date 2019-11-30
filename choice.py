from reader import periodic_table

#Analizing answer
def get_option(n_answer):
    if n_answer == 1:
        nAtomic = int(input("Número Atômico: "))
        print_result(nAtomic)
        input("Aperte Enter para voltar...\n\n")
        print("\x1b[2J")
    elif n_answer == 2:
        nameElement = str(input("Nome do Elemento: "))
        nAtomic = return_position_by_the_name(removeCharacteresEspeciais(nameElement.lower()))
        print_result(nAtomic)
        input("Aperte Enter para voltar...\n\n")
        print("\x1b[2J")
    elif n_answer == 3:
        symbolElement = str(input("Simbolo do Elemento: "))
        nAtomic = return_position_by_the_symbol(symbolElement.lower())
        print_result(nAtomic)
        input("Aperte Enter para voltar...\n\n")
        print("\x1b[2J")
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
def return_position_by_the_name(string_name_element):
    names_elements = []
    for i in range(0, len(list_periodic_table)):
        names_elements.append(removeCharacteresEspeciais(list_periodic_table[i][1].lower()))
    position_element = names_elements.index(string_name_element)
    return position_element + 1

def return_position_by_the_symbol(string_symbol_element):
    """
    symbols_elements = []
    for i in range(0, len(list_periodic_table)):
        symbols_elements.append(list_periodic_table[i][2].lower())
    position_element = symbols_elements.index(string_symbol_element)
    """
    for i in range(0, len(list_periodic_table)):
        if string_symbol_element == list_periodic_table[i][2].lower():
            position_element
    return position_element + 1
    
#Metod to remove characteres especiais of text
def removeCharacteresEspeciais(text):
    from unicodedata import normalize
    return normalize('NFKD', text).encode('ASCII','ignore').decode('ASCII')






