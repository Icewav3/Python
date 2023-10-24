# -*- coding: utf-8 -*-
"""
calculator

Created on Sun Oct 22 11:50:23 2023

@author: coled
"""
import re

def parse_equation(equation):
    # Define a regular expression pattern to match real numbers and operators
    pattern = r"([-+]?\d*\.\d+|[-+]?\d+|[-+*/!])"
    tokens = re.findall(pattern, equation)

    stack = []
    result = 0
    operator = None
    for token in tokens:
        if token in r"+-*/!":
            operator = token
        else:
            number = float(token)
            if operator:
                print(operator)
                if operator == r"+": #addition logic
                    result += number
                elif operator == r"-": #subtraction logic
                    result -= number
                elif operator == r"*": #multiplication logic
                    result *= number
                elif operator == r"/": #division logic
                    if number != 0:
                        result /= number
                    else:
                        print("Error: Division by zero")
                        return None
                elif operator == r"!": #count all values and add them
                    r = range(0, int(number) + 1)
                    for x in r:
                        result += x
                        
                operator = None #reset operator
            else: #return user input if no operators
                result = number

    return result

equation = input("Enter an equation: ")
result = parse_equation(equation)

if result is not None:
    print("Result:", result)

#MAIN
print("Enter a equation ")
input_str = input("Input: ")
output = parse_equation(input_str)
print(output)