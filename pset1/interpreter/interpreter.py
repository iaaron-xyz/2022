"""
USAGE:
$ python3 interpreter.py

DESCRIPTION:
In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then
calculates and outputs the result as a floating-point value formatted to one decimal place.
Assume that the user's input will be formatted as x y z, with one space between x and y and one space between y and z,
wherein:
x is an integer
y is +, -, *, or /
z is an integer
For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.
Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!

EXAMPLES:
$ python3 interpreter.py
Expression: 12 + 8
20.0

$ python3 interpreter.py
Expression: 3.14 - 1.14      
2.0
"""

def math_operation(operand1, operator, operand2):
    """[str, str, str]->float"""
    num1 = float(operand1)
    num2 = float(operand2)
    #  make the computation
    if operator == '+':
        r = num1 + num2
    elif operator == '-':
        r = num1 - num2
    elif operator == '*':
        r = num1 * num2
    elif operator == '/':
        r = num1 / num2
    else:
        r = "Operator not defined. Use: +, -, * or /."
    return r


def main():
    # Get the expression input by the user
    expression = input("Expression: ")
    # Split elements in one array
    expression_arr = expression.split()
    # Compute according to the operator
    print(math_operation(expression_arr[0], expression_arr[1], expression_arr[2]))


if __name__ == "__main__":
    main()