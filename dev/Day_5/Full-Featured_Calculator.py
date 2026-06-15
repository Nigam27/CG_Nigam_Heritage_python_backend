# Scientific_Calculator.py

try:
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))

    operator = input("Enter operator (+, -, *, /): ")

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            result = num1 / num2
    else:
        print("Invalid operator!")
        exit()

    if operator != "/" or num2 != 0:
        print("Result =", result)

except ValueError:
    print("Error: Please enter valid numbers only!")