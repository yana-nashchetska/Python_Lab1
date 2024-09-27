from functions.check_operator import check_operator


def input_operator():
    oper = input("Введіть оператор: ")
    oper = check_operator(oper)
    return oper
