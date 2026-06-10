# SYNTAX: print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
 
# Basic usage
print("Hello, World!")
 
# Multiple values — separated by space (default)
print("Name:", "Amit", "Age:", 30)
# Output: Name: Amit Age: 30
 
# Custom separator using sep=
print("2024", "01", "15", sep="-")
# Output: 2024-01-15
 
print("Mumbai", "Maharashtra", "India", sep=" | ")
# Output: Mumbai | Maharashtra | India
 
# Custom end character using end=
print("Loading", end="")
print("...", end="")
print(" Done!")
# Output: Loading... Done!  (all on ONE line)
 
# Printing blank line
print()
# Output: (empty line)
 
# Printing numbers and expressions
print(2 + 3)
print(10 * 5)
print(100 / 4)
