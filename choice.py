from reader import periodic_table

#Analizing answer
def get_option(answer):
    if answer == 1:
        n_atomic = int(input("Número atômico: "))
        print_result(n_atomic)
    elif answer == 2:
        name_element = str(input("Nome do elemento: "))
        name_element = remove_characteres_especials(name_element)
        n_atomic = return_position_by_the_name(name_element)
        print_result(n_atomic)
    elif answer == 3:
        symbol_element = str(input("Símbolo do elemento: "))
        n_atomic = return_position_by_the_symbol(symbol_element)
        print_result(n_atomic)
    elif answer == 4:
        atomic_weight_element = float(input("Massa Atômica: "))
        n_atomic = return_position_by_the_atomic_weight(atomic_weight_element)
        print_result(n_atomic)
    elif answer == 5:
        pass
    elif answer == 6:
        for i in range(0, len(periodic_table['Atomic Number'])):
            print_result(i + 1)
    elif answer == 0:
        pass

# Show with base in answer
def print_result(value):
    print(f"""
===================================================
    Número Atômico: {periodic_table['Atomic Number'][value - 1]}
    Nome do Elemento: {periodic_table['Element'][value - 1]}
    Símbolo: {periodic_table['Symbol'][value - 1]}
    Massa Atômica: {periodic_table['Atomic Weight'][value - 1]}
    Estado Físico Natural: {periodic_table['Phase'][value - 1]}
    Distribuição Eletrônica: {periodic_table['Electron Configuration'][value - 1]}
===================================================
    """)
    print("Clique \"ENTER\" para avançar...")
    input()

def remove_characteres_especials(text):
    from unicodedata import normalize
    return normalize('NFKD', text).encode('ASCII','ignore').decode('ASCII')

def return_position_by_the_name(string_name_element):
    names = []
    for number in range(0, len(periodic_table['Element'])):
        names.append(remove_characteres_especials(periodic_table['Element'][number].lower()))
    return names.index(string_name_element.lower()) + 1

def return_position_by_the_symbol(string_symbol_element):
    symbols = []
    for number in range(0, len(periodic_table['Symbol'])):
        symbols.append(periodic_table['Symbol'][number].lower())
    return symbols.index(string_symbol_element.lower()) + 1

def return_position_by_the_atomic_weight(float_atomic_weight_element):
    atomics_weights = []
    for number in range(0, len(periodic_table['Atomic Weight'])):
        atomics_weights.append(round(float(periodic_table['Atomic Weight'][number])))
    return atomics_weights.index(round(float_atomic_weight_element)) + 1








