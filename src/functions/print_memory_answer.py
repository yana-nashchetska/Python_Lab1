def show_memory_answer(answer):
   while True:
       match answer:
        case '1':
            print("Пам'ять очищена.")
        case '2':
            print(f"Значення в пам'яті виведено.")
        case '3':
            print("Значення збережено.")
        case '4':
            print("Значення додано.")
        case '5':
            break
        case _:
            print('Такого варіанта меню не існує.')
    