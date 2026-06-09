# case_sensitivity.py

# Case sensitivity demonstration

name = "Rahul"

Name = "Rahul Sharma"

NAME = "R. SHARMA"


print(name)   # Rahul

print(Name)   # Rahul Sharma

print(NAME)   # R. SHARMA


# These are THREE completely different variables!


# Common mistake:

counter = 0

Counter = counter + 1    # This creates a NEW variable 'Counter'

print(counter)           # Still 0 — original unchanged!

print(Counter)           # 1