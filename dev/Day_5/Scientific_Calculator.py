# Version 2: Extended operators
print("Operators: + - * / // % **")
num1 = float(input("First number : "))
op = input("Operator : ")
num2 = float(input("Second number: "))
ops = {
 "+" : num1 + num2,
 "-" : num1 - num2,
 "*" : num1 * num2,
 "/" : num1 / num2 if num2 != 0 else "Div by 0",
 "//" : num1 // num2,
 "%" : num1 % num2,
 "**" : num1 ** num2,
}
result = ops.get(op, "Invalid operator")
print(f"{num1} {op} {num2} = {result}")