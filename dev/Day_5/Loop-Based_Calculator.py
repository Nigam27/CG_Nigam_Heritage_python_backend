# Version 3: Continuous Calculator
print("=" * 35)
print(" Python Calculator (type q to quit)")
print("=" * 35)
while True:
 expr = input("\nEnter expression (e.g. 5 + 3): ")
 if expr.lower() == "q":
    print("Goodbye!")
 break
try:
 parts = expr.split()
 a, op, b = float(parts[0]), parts[1], float(parts[2])
 if op == "+": r = a + b
 elif op == "-": r = a - b
 elif op == "*": r = a * b
 elif op == "/": r = a / b if b != 0 else "Error"
 else: r = "Unknown op"
 print(f" = {r}")
except:
 print("Invalid input. Try: 5 + 3")