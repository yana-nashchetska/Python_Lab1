from app_settings import get_console_color

def print_memory_menu():
    color = get_console_color()
    print(color + '1. Очистити пам\'ять')
    print(color + '2. Викликати пам\'ять')
    print(color + '3. Зберегти в пам\'ять')
    print(color + '4. Додати до пам\'яті')
    print(color + '5. Назад')
    
    answer = input()
    return answer
