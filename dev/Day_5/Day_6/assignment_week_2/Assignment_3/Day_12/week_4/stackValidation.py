expression = "((A+B)*(C-D))"

stack = []
balanced = True

for ch in expression:
    if ch == '(':
        stack.append(ch)
    elif ch == ')':
        if len(stack) == 0:
            balanced = False
            break
        stack.pop()

if len(stack) != 0:
    balanced = False

if balanced:
    print("Balanced")
else:
    print("Not Balanced")