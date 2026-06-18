phonebook = {'Alice': '9876543210', 'Bob': '8765432109'}
# Direct access — CRASHES if key missing
# print(phonebook['Carol']) → KeyError: 'Carol'
# Safe access with get()
print(phonebook.get('Alice')) # 9876543210
print(phonebook.get('Carol')) # None (no error!)
print(phonebook.get('Carol', 'Not found')) # Not found
# Real use: inventory stock check
inventory = {'apple': 50, 'mango': 0}
item = 'banana'
stock = inventory.get(item, 0) # default 0 if not found
if stock > 0:
 print(f'{item} available: {stock}')
else:
 print(f'{item} out of stock')
# banana out of stock
