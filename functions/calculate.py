from functions.check_number import check_number
from functions.calc_result import calc_result
from functions.check_operator import check_operator
from functions.history import add_to_history
from AppSettings import get_decimal

def calculate():
    print(" --- Введіть дані: ---")
    number1 = input("Перше число: ")
    number1 = check_number(number1)
    
    potential_operator = input("Введіть знак: ")
    operator = check_operator(potential_operator)

    if operator == "sqrt":
        result = calc_result(number1, operator)
        expression = f"{operator}({number1})"
    else:
        number2 = input("Друге число: ")
        number2 = check_number(number2)
        result = calc_result(number1, operator, number2)
        expression = f"{number1} {operator} {number2}"

    decimal_places = get_decimal()
    result = round(result, decimal_places)
    add_to_history(expression, result)
    print(f"Result is: {result:.{decimal_places}f}")
