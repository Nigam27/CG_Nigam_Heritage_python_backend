salaries = {'Alice': 75000, 'Bob': 85000, 'Carol': 70000}
# keys() — all keys
print(salaries.keys()) # dict_keys(['Alice', 'Bob', 'Carol'])
# values() — all values
print(salaries.values()) # dict_values([75000, 85000, 70000])
# items() — key-value pairs as tuples
print(salaries.items())
# dict_items([('Alice', 75000), ('Bob', 85000), ('Carol', 70000)])
# Loop with items() — most common pattern
for name, salary in salaries.items():
 print(f'{name}: ₹{salary:,}')
# Total salary budget
total = sum(salaries.values())
print(f'Total Budget: ₹{total:,}') # ₹2,30,000
# Find highest earner
top_earner = max(salaries, key=salaries.get)
print(f'Highest earner: {top_earner}') # Bob