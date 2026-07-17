#The Continuous Scientific Calculator 

import math
while True:
    choice = input("Choose an operation to perform: (+, -, *, /, sin, cos) or type 'end' to exit: ")
    if choice == "end":
        print("Calculator shutting down ")
        break

    if choice == "+":
        a = float(input("Enter your first number:"))
        b = float(input("Enter your second number:"))
        print("Result:", a+b)

    elif choice == "-":
        a = float(input("Enter your first number:"))
        b = float(input("Enter your second number:"))
        print("Result:", a-b)

    elif choice == "*":
        a = float(input("Enter your first number:"))
        b = float(input("Enter your second number:"))
        print("Result:", a*b)

    elif choice == "/":
        a = float(input("Enter your first number:"))
        b = float(input("Enter your second number:"))
        if b == 0:
            print("It cannot be divided by zero")
        else:
            print("Result:", a/b)

    elif choice == "sin":
        x = float(input("Enter  your number:"))
        angle = input("Enter d for degrees or r for radians:")
        if angle == "d":
            x = math.radians(x)
        print("Result:", math.sin(x))

    elif choice == "cos":
        x = float(input("Enter  your number:"))
        angle = input("Enter d for degrees or r for radians:")
        if angle == "d":
            x = math.radians(x)
        print("Result:", math.cos(x))

    else:
        print("Invalid operator. Plz enter the right operator.")