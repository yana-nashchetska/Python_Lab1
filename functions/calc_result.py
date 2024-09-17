from constants.GlobalVariables import MainButton, AdditionalButton
from functions.operations_functions import *

def calc_result(num1, oper, num2 = 0):
    a = float(num1)
    b = float(num2)

    match oper:
          case MainButton.ADDITION.value:
               return add(a, b)
          case MainButton.SUBTRACTION.value:
                return subtract(a, b)
          case MainButton.MULTIPLICATION.value:
                return multiply(a, b)
          case MainButton.DIVISION.value:
                return divide(a, b)
          case AdditionalButton.SQRT.value:
                return find_sqrt(a)
          case AdditionalButton.REMAINDER.value:
                return find_remainder(a, b)
          case AdditionalButton.POWER.value:
                return to_power(a, b)
