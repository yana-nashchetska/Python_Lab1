import app_settings
from classes.ConsoleReader import ConsoleReader
from classes.Calculator import Calculator
from classes.ConsoleWriter import ConsoleWriter
from constants.global_variables import main_menu, memory_menu, settings_menu
from functions.menu_functions import print_menu


class CalculatorConsole:
    def __init__(self):
        self.consoleWriter = ConsoleWriter()
        self.consoleReader = ConsoleReader()
        self.calculator = Calculator()

    def run_console(self):

        while True:
            print_menu(app_settings.console_color, main_menu)
            answer = self.consoleReader.read_value("Оберіть варіант меню")
            answer = self.consoleReader.check_value(answer, "number")

            match answer:
                case 1:
                    param_1 = self.consoleReader.read_value("Введіть перше число")
                    param_1 = self.consoleReader.check_value(param_1, "number")

                    operator = self.consoleReader.read_value("Введіть оператор")
                    operator = self.consoleReader.check_value(operator, "operator")

                    param_2 = self.consoleReader.read_value("Введіть друге число")
                    param_2 = self.consoleReader.check_value(param_2, "number")

                    result = self.calculator.calc(param_1, operator, param_2)
                    result = round(result, int(app_settings.decimal_places))
                    self.calculator.current_value = result
                    self.calculator.add_to_history(param_1, operator, param_2, result)

                case 2:
                    self.consoleWriter.output_value(
                        self.calculator.current_value, "Відповідь"
                    )

                case 3:
                    self.consoleWriter.output_value(self.calculator.history, "Історія")

                case 4:
                    self.handle_settings_menu()

                case 5:
                    self.handle_memory_menu()

                case _:
                    self.consoleWriter.output_value(
                        answer, "Такого варіанта в меню немає"
                    )
            continue_answer = self.consoleReader.read_value('Продовжити? (так/ні)')
            if continue_answer == 'ні':
                break
        

    def handle_settings_menu(self):
        while True:
            print_menu(app_settings.console_color, settings_menu)
            option = self.consoleReader.read_value("Оберіть варіант меню")
            option = self.consoleReader.check_value(option, "number")

            match option:
                case 1:
                    new_decimal = self.consoleReader.read_value(
                        "Введіть нову кількість знаків після коми"
                    )
                    new_decimal = self.consoleReader.check_value(new_decimal, "number")

                    app_settings.set_decimal(new_decimal)
                    self.consoleWriter.output_value(
                        app_settings.decimal_places,
                        "Кількість знаків після коми змінено на",
                    )

                case 2:
                    self.consoleWriter.output_value(
                        app_settings.console_color, "Поточний колір консолі"
                    )
                    new_color = self.consoleReader.read_value(
                        """Введіть новий колір.
                            Доступні кольори:
                            black, red, green, yellow, blue, magenta, cyan, white
                        """
                    )

                    new_color = self.consoleReader.check_value(new_color, "color")
                    app_settings.set_console_color(new_color)
                    self.consoleWriter.output_value(
                        app_settings.console_color, "Колір консолі змінено на"
                    )

                case 3:
                    break

                case _:
                    self.consoleWriter.output_value(
                        option, "Такого ваіанта в меню немає"
                    )

    def handle_memory_menu(self):
        while True:
            print_menu(app_settings.console_color, memory_menu)

            option = self.consoleReader.read_value("Оберіть варіант меню")
            option = self.consoleReader.check_value(option, "number")

            match option:
                case 1:
                    self.calculator.memory = 0
                case 2:
                    self.consoleWriter.output_value(
                        self.calculator.memory, "Поточне значення"
                    )
                case 3:
                    self.calculator.memory = self.consoleReader.read_value(
                        "Введіть нове значення пам'яті"
                    )
                case 4:
                    new_value = self.consoleReader.read_value(
                        "Додати в пам'ять таке значення"
                    )
                    new_value = self.consoleReader.check_value(new_value, "number")

                    self.calculator.memory += new_value

                case 5:
                    break
                case _:
                    self.consoleWriter.output_value(
                        option, "Такого ваіанта в меню немає"
                    )
