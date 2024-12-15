from art import logo

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operators = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}

def calculator():
    print(logo)
    print()
    num1 = float(input("What is the first number ? : "))

    for operator in operators:
        print(operator)

    terminate = ""
    while terminate != 'n':
        symbol = input("Pick an operation from the line above: ")
        calculate = operators[symbol]
        num = float(input("What is the next number? : "))
        answer = calculate(num1, num)
        print(f"{num1} {symbol} {num} = {answer}")
        num1 = answer
        terminate = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start anew: ")
        if terminate == 'n':
            calculator();

calculator()
