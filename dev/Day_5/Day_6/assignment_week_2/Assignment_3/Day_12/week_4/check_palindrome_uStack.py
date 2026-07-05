string = "MADAM"

stack = []

for ch in string:
    stack.append(ch)
reverse = ""

while len(stack) != 0:
    reverse += stack.pop()
if string == reverse:
    print("Yes,Palindrome")
else:
    print("Not Palindrome")