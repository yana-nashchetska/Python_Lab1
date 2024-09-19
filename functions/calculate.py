from functions.check_number import check_number
from functions.calc_result import calc_result
from functions.check_operator import check_operator

def calculate():
    print(" --- Введіть дані: ---")
    number1 = input("Перше число: ")
    number1 = check_number(number1)
    
    potential_operator = input("Введіть знак: ")
    operator = check_operator(potential_operator)

    if operator == "sqrt":
        result = calc_result(number1, operator)
    else:
        number2 = input("Друге число: ")
        number2 = check_number(number2)
        result = calc_result(number1, operator, number2)

    print("Result is: " + str(result))
