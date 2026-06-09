
# VALID identifiers — these work

age = 25
first_name = "Anjali"
account_balance = 50000.00
is_logged_in = True
_private_var = "hidden"
myVariable123 = "value"
TotalCount = 100

print("age =", age)
print("first_name =", first_name)
print("account_balance =", account_balance)
print("is_logged_in =", is_logged_in)
print("_private_var =", _private_var)
print("myVariable123 =", myVariable123)
print("TotalCount =", TotalCount)

# INVALID identifiers — these cause SyntaxError

# 2name = "Raj"         # Cannot start with a number
# first-name = "Priya"  # Hyphens not allowed
# class = "Python"      # 'class' is a keyword
# my variable = 10      # No spaces allowed
# @email = "a@b.com"    # Special characters not allowed