from menu import show_menu
from choice import get_option

answer = None

while answer != 0:
    show_menu()
    answer = int(input('--> '))
    # TODO melhorar filtro por distribuição
    get_option(answer)
