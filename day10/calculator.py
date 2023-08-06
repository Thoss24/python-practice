
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b

operators = {"+": add, "-": subtract, "/": divide, "*": multiply}

def calculator():
    num1 = float(input("First Number: "))
    proceed = True

    while proceed:
        operator = input("Choose an operator i.e., '+', '-', '*', '/': ")
        num2 = float(input("Second Number: "))
        operations_function = operators[operator]
        answer = operations_function(num1, num2)
        print(f"{num1} {operator} {num2} = {answer}")
        again = input("Want to proceed? 'y' for yes 'n' for no: ")
        if again == 'y':
            num1 = answer
        else:
            proceed = False
            calculator()
        
calculator()