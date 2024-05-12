#Print Calculator ASCII art logo
from art import logo
print(logo)

#Add function
def add(n1, n2):
    return n1 +n2

#Subtract function
def substract(n1, n2):
    return n1 - n2

#Multiply function
def multiply(n1, n2):
    return n1 * n2

#Divide function
def divide(n1, n2):
    return n1 / n2

#Dictionary of math operations
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("What's the first number?: "))
    calculating = True

    while calculating is True:
        #For loop to display the operations symbols
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above: ")

        num2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        should_continue = input(f"Do you want to continue with {answer}? Type 'y' to continue and 'n' to start a new calculation. ")
        
        if should_continue == "y":
            num1 = answer
        else:
            calculating = False
            #Recursion: recalling the same function again
            calculator()

calculator()