def check_number(num):
    if isinstance(num, str) and num.isnumeric():
        num = float(num)
    else:
        num = input('Помилка. Введіть число: ')

        return check_number(num)

    return num

