def output_value(value):
    try:
        print("Ваше значення: ", float(value))
    except ValueError:
        print("Помилка: значення не є числом.")
