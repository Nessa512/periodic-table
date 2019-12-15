from reader import periodic_table

#Analizing answer
def get_option(answer):
    if answer == 1:
        try:
            n_atomic = int(input("Número atômico: "))
            if ((n_atomic > 0) and (n_atomic < 119)):
                print_result(n_atomic)
            else:
                return ValueError
        except KeyboardInterrupt:
            pass
        except ValueError:
            print(f'Nenhum elemento químico tem número atômico: {n_atomic}')
            print('0 < nAtomico < 119')
            input('\"ENTER\" para voltar ao menu...\n')
    elif answer == 2:
        try:
            name_element = str(input("Nome do elemento: "))
            name_element = remove_characteres_especials(name_element)
            n_atomic = return_position_by_the_name(name_element)
            print_result(n_atomic)
        except KeyboardInterrupt:
            pass
        except:
            print(f'Nome \"{name_element.title()}\" não encontrado...')
            input('\"ENTER\" para voltar ao menu...\n')
    elif answer == 3:
        try:
            symbol_element = str(input("Símbolo do elemento: "))[:2]
            n_atomic = return_position_by_the_symbol(symbol_element)
            print_result(n_atomic)
        except KeyboardInterrupt:
            pass
        except:
            print(f'Simbolo \"{symbol_element.title()}\" não encontrado...')
            input('\"ENTER\" para voltar ao menu...\n')
    elif answer == 4:
        try:
            atomic_weight_element = float(input("Massa Atômica: "))
            n_atomic = return_position_by_the_atomic_weight(atomic_weight_element)
            print_result(n_atomic)
        except KeyboardInterrupt:
            pass
        except:
            print(f'Nenhum elemento químico tem massa atômica igual a: {atomic_weight_element}')
            input('\"ENTER\" para voltar ao menu...\n')
    elif answer == 5:
        try:
            for i in range(0, len(periodic_table['Atomic Number'])):
                print_result(i + 1)
        except KeyboardInterrupt:
            pass
    elif answer == 6:
		try:
			for i in range(0, len(periodic_table['Atomic Number'])):
			    print_result(i + 1)
		except KeyboardInterrupt:
			pass
    elif answer == 0:
        print('Bye bye! 👍')

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
    input("Clique \"ENTER\" para avançar...\nCtrl + C para sair...\n")

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








