try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    print("What operation would you like to perform? (+, -, *, /)")

    o = input("Enter the operation: ")

    match o:
        case "+":
            print(f"The result of {a} + {b} is: {a + b}")
        case "-":
            print(f"The result of {a} - {b} is: {a - b}")
        case "*":
            print(f"The result of {a} * {b} is: {a * b}")
        case "/":   
            if b != 0:
                print(f"The result of {a} / {b} is: {a / b}")
            else:
                print("Error: Division by zero is not allowed.")
        case _:
            print("Invalid operation. Please enter one of the following: +, -, *, /")

except :
    print("Invalid input. Please enter numeric values.")
    exit()
