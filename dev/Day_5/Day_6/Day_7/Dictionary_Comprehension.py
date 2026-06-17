# Square each number
squares = {x: x**2 for x in range(1, 6)}
print(squares) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# Filter — only expensive products
prices = {'apple': 40, 'mango': 120, 'banana': 20, 'grape': 180}
expensive = {item: p for item, p in prices.items() if p > 50}
print(expensive) # {'mango': 120, 'grape': 180}
# Apply 10% GST to all prices
with_gst = {item: round(p * 1.10, 2) for item, p in prices.items()}
print(with_gst) # {'apple': 44.0, 'mango': 132.0, ...}
# Invert a dictionary (swap keys and values)
original = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in original.items()}
print(inverted) # {1: 'a', 2: 'b', 3: 'c'}