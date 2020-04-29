"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, add_mult, add_cubes)


# Replace this with your code
def translate(tokens):
    if tokens[0] == "+":
        return add(float(tokens[1]), float(tokens[2]))
    elif tokens[0] == "-":
        return subtract(float(tokens[1]), float(tokens[2]))
    elif tokens[0] == "*":
        return multiply(float(tokens[1]), float(tokens[2]))
    elif tokens[0] == "/":
        return divide(float(tokens[1]), float(tokens[2]))
    elif tokens[0] == "square":
        return square(float(tokens[1]))
    elif tokens[0] == "cube":
        return cube(float(tokens[1]))
    elif tokens[0] == "pow":
        return power(float(tokens[1]), float(tokens[2]))
    elif tokens[0] == "mod":
        return mod(float(tokens[1]), float(tokens[2]))
    elif tokens[0] == "x+":
        return add_mult(float(tokens[1]), float(tokens[2]), float(tokens[3]))
    elif tokens[0] == "cubes+":
        return add_cubes(float(tokens[1]), float(tokens[2]))
    else:
        return "Please enter a valid operator."

def validate(tokens):
    if token[0] not in ["+", "-", "*", "/", "square", "cube", "pow", "mod", "x+", "cubes+"]:
        print("Please enter a valid operator.")
    elif token[0] in ["+", "-", "*", "/", "pow", "mod", "cubes+"] and len(tokens) =! 3:
        print(f"The {token[0]} operator requires two operands.")
    elif token[0] in ["square", "cube"] and len(tokens) =! 2:
        print(f"The {token[0]} operator takes exactly one operand.")
    elif token[0]=="x+" and len(tokens) =! 4:
        print("The x+ operator requires three operands.")
    else:
        return True
    return False

while True:
    equation = input("Enter your equation > ")
    tokens = equation.split(" ")
    if not isValid(tokens):
        continue
    if equation == "q" or equation == "quit":
        break
    if len(tokens) < 3:
        print("Not enough inputs.")
        continue
    print(translate(tokens))





