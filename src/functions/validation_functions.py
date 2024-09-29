from constants.global_variables import Button, Color


def check_number(param):
    try:
        return float(param)
    except ValueError:
        print(f"'{param}' не є числом. Введіть число.")
        return check_number(input("Введіть число: "))


# злити в одну функцію check_string


def check_operator(potential_op):
    available_operators = [symbol.value for symbol in Button]
    if potential_op not in available_operators:
        print("Помилка. Введіть знак ще раз.")
        return check_operator(input("Введіть знак: "))
    return potential_op


def check_color(potential_color):
    available_colors = [symbol.value for symbol in Color]
    if potential_color not in available_colors:
        print("Помилка. Введіть колір ще раз.")
        return check_color(input("Введіть колір: "))
    return potential_color
