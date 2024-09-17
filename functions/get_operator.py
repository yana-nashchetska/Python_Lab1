from constants.GlobalVariables import MainButton, extended, AdditionalButton

def get_operator(potential_op):
    global extended
    while True:
        available_operators = [symbol.value for symbol in MainButton]

        # Якщо розширене меню ввімкнене, додаємо додаткові оператори
        #  додала not, чомусь працює........
        if extended: 
            available_operators += [symbol.value for symbol in AdditionalButton]

        # Перевіряємо, чи введений оператор належить до доступних
        if potential_op not in available_operators:
            potential_op = input('Помилка. Введіть знак ще раз: ')
        else:
            break

    return potential_op
    
    # print(extended)

