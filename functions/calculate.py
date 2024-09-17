from constants.GlobalVariables import AdditionalButton, MainButton, extended
from functions.calc_result import calc_result
from functions.get_operator import get_operator

def calculate():
    global extended
    print(" --- Введіть дані: ---")
    number1 = float(input("Перше число: "))
    potential_operator = input("Введіть знак: ")

    # Обираємо оператор
    operator = get_operator(potential_operator)

    # Якщо оператор в основному меню
    if operator in [op.value for op in MainButton]:
        number2 = float(input("Друге число: "))
        result = calc_result(number1, operator, number2)

    # Якщо оператор в додатковому меню
    elif operator in [op.value for op in AdditionalButton]:
        if operator == "sqrt":  # Приклад для квадратного кореня
            result = calc_result(number1, operator)
        else:
            number2 = float(input("Друге число: "))
            result = calc_result(number1, operator, number2)

    else:
        print("Помилка. Невідомий оператор.")
        return

    # Виведення результату
    print("Result is: " + str(result))
    return
