# Version 1: Basic 2-number Calculator
num1 = float(input("Enter first number : "))
operator = input("Enter operator (+,-,*,/) : ")
num2 = float(input("Enter second number: "))
if operator == "+":
 result = num1 + num2
elif operator == "-":
 result = num1 - num2
elif operator == "*":
 result = num1 * num2
elif operator == "/":
 if num2 != 0:
    result = num1 / num2
 else:
    result = "Error: Division by zero!"
else:
 result = "Unknown operator"
print(f"Result: {num1} {operator} {num2} = {result}")
