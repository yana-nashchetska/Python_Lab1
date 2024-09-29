from functions.new_functions.read_from_input import read_from_input
from functions.new_functions.validation_functions import check_color, check_number, check_operator

class ConsoleReader:
    def read_value(self, message=""):
        return read_from_input(f'{message}: ')
    
    def check_value(self, value, value_type="number"):
        match value_type:
            case "number":
                return check_number(value)
            case "operator":
                return check_operator(value)
            case "color":
                return check_color(value)
            case _:
                raise ValueError(f"Невідомий тип: '{value_type}'.")

