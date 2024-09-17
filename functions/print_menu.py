from functions import toggle_extended
from functions import calc_result
from functions import calculate
from functions import get_operator
from functions import open_settings
from functions import operations_functions
from functions import print_menu
from functions import show_history
from constants.GlobalVariables import extended

def print_menu():
    global extended  # Додаємо global для доступу до змінної extended
    while True:
        print('1. Обчислити')
        print('2. Історія')
        print('3. Налаштування')
        print('4. Додаткові операції')
        print('5. Вийти')


        answer = input()

        match answer:
            case '1':
                calculate()
            case '2':
                show_history()
            case '3':
                open_settings()
            case '4':
                # change_extended()  # Змінюємо режим
                # print(f"extended після зміни: {extended}")  # Перевіряємо extended
                # # Викликаємо calculate з урахуванням нового значення extended
                # calculate()
                toggle_extended.toggle_extended()  # Змінюємо режим
                print(extended)
            case '5':
                break
            case _:
                print('Такого варіанта меню не існує.')
