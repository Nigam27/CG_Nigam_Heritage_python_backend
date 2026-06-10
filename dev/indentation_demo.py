# WRONG — missing indentation causes IndentationError
age = 20
if age >= 18:
print('You are an adult')    # ❌ Error: expected indented block
 
# CORRECT — 4 spaces of indentation
age = 20
if age >= 18:
    print('You are an adult')    # ✅ Correct — 4 spaces
    print('You can vote!')
print('This runs always')   # Back to no indentation = outside the if block
