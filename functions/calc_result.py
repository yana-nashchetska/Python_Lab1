from constants.GlobalVariables import Button
from functions.operations_functions import *

def calc_result(num1, oper, num2 = 0):
    a = float(num1)
    b = float(num2)

    match oper:
          case Button.ADDITION.value:
               return add(a, b)
          case Button.SUBTRACTION.value:
                return subtract(a, b)
          case Button.MULTIPLICATION.value:
                return multiply(a, b)
          case Button.DIVISION.value:
                return divide(a, b)
          case Button.SQRT.value:
                return find_sqrt(a)
          case Button.REMAINDER.value:
                return find_remainder(a, b)
          case Button.POWER.value:
                return to_power(a, b)
