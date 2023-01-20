'''simple calculator to perform basic arithmatic operations to include additon, subtraction, mulitplication, division
and a bit of caveat with square root and exponential '''

from art import logo
import math

# Defining arithmatic operations into respecitive functions
#Addition
def add(num1, num2):
    return num1 + num2

#Subtraction
def subtract(num1, num2):
    return num2 - num1

#Mulitplication
def multiply(num1, num2):
    return num1 * num2

#Division
def divide(num1, num2):
    return num1 / num2

#Square Root
def sqrt(num1):
    return math.sqrt(num1)

#Exponetial
def exp(num1, num2):
    return num1 ** num2

'''Setting up dictionary linking the symoblic operators to respective functions '''
operators = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide,
    'sqrt': sqrt,
    '^' : exp,
}


'''Defining Calculator funciton'''
def calculator():
    print(logo)
    num1 = float(input("Input the first number: "))
    #Looping over the dictionary to print the operator choices to choose from
    for operand in operators:
        print(operand)
    #setting Continuity variable before defining the while loop for continuous calculations
    cont = True
    #Defining while loop for continuing calculations
    while cont:
        operator = input("Type desired operation: ")
        if operator == "sqrt":
            result = operators[operator](num1)
            print(f"{operand} {num1} = {result}")
        else:
            num2 = float(input("Input the next number: "))
            result = operators[operator](num1, num2)
            print(f"{num1} {operand} {num2} = {result}")
        
        if (input("Continue calculations with answer? type 'y' or type 'n' to start a new calculation: ")) == "y":
            #For continuing calculation result value becomes the first number
            num1 = result
        # Break out of the loop to start a new calculation
        else:
            cont = False
            #Recursive function
            calculator()

#Calling calculator function
calculator()