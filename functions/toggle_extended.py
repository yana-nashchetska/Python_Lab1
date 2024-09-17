from constants.GlobalVariables import extended

def toggle_extended():
    global extended
    extended = 2
     
    print('extended from change: ', extended)
    # if extended == True:
    #     print("Вам доступні операції розширеного меню (sqrt, %, ^).")
    # else:
    #     print("Розширене меню вимкнене.")
    
    # Додаємо додатковий друк для перевірки
    # print(f"Режим розширеного меню: {extended}")
