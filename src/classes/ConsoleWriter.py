from functions.new_functions.write_to_output import write_to_output

class ConsoleWriter:
    def output_value(self, value, message="Ваше значення"):
        write_to_output(f"{message}: {value}")