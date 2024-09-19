from functions.calculate import calculate
from functions.open_settings import open_settings
from functions.show_history import show_history

def print_menu():
    while True:
        print('1. Обчислити')
        print('2. Історія')
        print('3. Налаштування')
        print('4. Вийти')

        answer = input()

        match answer:
            case '1':
                calculate()
            case '2':
                show_history()
            case '3':
                open_settings()
            case '4':
                break
            case _:
                print('Такого варіанта меню не існує.')
