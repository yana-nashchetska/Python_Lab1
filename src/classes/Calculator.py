from app_settings import get_console_color, get_decimal
from constants.GlobalVariables import Button
from functions.input_number import input_number
from functions.input_operator import input_operator
from functions.output_value import output_value
from functions.output_history import output_history
from functions.print_memory_menu import print_memory_menu
from functions.output_settings import output_settings
from functions.operations_functions import (
    add,
    subtract,
    multiply,
    divide,
    find_sqrt,
    find_remainder,
    to_power,
)


class Calculator:
    a = 0
    b = 0
    operator = ""

    def __init__(self, current_value=0, memory=0):
        self.current_value = current_value
        self.memory = memory
        self.history = []

    def add_to_history(self, operation, result):
        self.history.append(f"{operation} = {result}")

    def show_history(self):
        output_history(self.history)

    def input_data(self):
        self.a = input_number()
        self.operator = input_operator()

        if not self.operator == "sqrt":
            self.b = input_number()

    def check_operator(potential_op):
        while True:
            available_operators = [symbol.value for symbol in Button]

            if potential_op not in available_operators:
                potential_op = input_operator()
            else:
                break

        return potential_op

    def calculate(self):
        self.input_data()

        a = float(self.a)
        b = float(self.b) if self.operator != "sqrt" else 0
        oper = self.operator

        operations = {
            Button.ADDITION.value: add,
            Button.SUBTRACTION.value: subtract,
            Button.MULTIPLICATION.value: multiply,
            Button.DIVISION.value: divide,
            Button.SQRT.value: find_sqrt,
            Button.REMAINDER.value: find_remainder,
            Button.POWER.value: to_power,
        }

        try:
            if oper in operations:
                if oper == Button.SQRT.value:
                    result = operations[oper](a)
                    self.current_value = result
                    expression = f"{self.operator}({self.a})"
                else:
                    if oper == Button.DIVISION.value and b == 0:
                        raise ZeroDivisionError("Помилка: Ділення на нуль!")

                    result = operations[oper](a, b)
                    expression = f"{self.a} {self.operator} {self.b}"
                    decimal_places = get_decimal()
                    result = round(result, decimal_places)
                    self.current_value = result
                    self.add_to_history(expression, result)
            else:
                raise ValueError("Неправильний оператор")

            self.show_result()  # Вивести результат після обчислень

        except ZeroDivisionError as e:
            self.current_value = str(e)
            self.show_result()  # Вивести повідомлення про помилку
        except ValueError as e:
            self.current_value = str(e)
            self.show_result()
        except Exception as e:
            self.current_value = f"Сталася помилка: {str(e)}"
            self.show_result()

    def show_result(self):
        output_value(self.current_value)

    def memory_clear(self):
        self.memory = 0

    def memory_recall(self):
        decimal_places = get_decimal()
        return round(self.memory, decimal_places)

    def memory_store(self, value):
        self.memory = value

    def memory_add(self, value):
        if isinstance(value, (int, float)):
            self.memory += value
            decimal_places = get_decimal()
            self.memory = round(self.memory, decimal_places)
        else:
            raise ValueError("Значення повинно бути числом.")

    def open_settings(self):
        output_settings()

    def open_memory_menu(self):
        while True:
            answer = print_memory_menu()
            match answer:
                case "1":
                    self.memory_clear()
                case "2":
                    output_value(self.memory_recall())
                case "3":
                    value = input_number()
                    self.memory_store(value)
                case "4":
                    value = input_number()
                    self.memory_add(value)
                case "5":
                    break
                case _:
                    print("Такого варіанта меню не існує.")

    def run_calculator(self):
        color = get_console_color()
        while True:
            print(
                color
                + "1. Ввести дані\n2. Вивести результат\n3. Історія\n4. Налаштування\n5. Пам'ять\n6. Вийти\n"
            )
            answer = input()
            match answer:
                case "1":
                    self.calculate()
                case "2":
                    self.show_result()
                case "3":
                    self.show_history()
                case "4":
                    self.open_settings()
                case "5":
                    self.open_memory_menu()
                case "6":
                    break
                case _:
                    print("Такого варіанта меню не існує.")
