#Calculator
from art import logo

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2
    
#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

#a dictionary as a means to call the functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    
    num1 = float(input("Whats the first number?: "))
    for symbol in operations:
        print(symbol)
        
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("Whats the next number?: "))
        #use the chosen symbol as key to pick the desired operaration from the dictionary
        calculation_function = operations[operation_symbol]
        #call the corresponding function and pass the numbers as arguments
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation.: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
calculator()
