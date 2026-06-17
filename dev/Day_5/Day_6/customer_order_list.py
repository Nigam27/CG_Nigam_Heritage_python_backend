orders = ['Order#101', 'Order#102', 'Order#103']
# Basic for loop
for order in orders:
 print(f'Processing: {order}')
# With index using enumerate()
for i, order in enumerate(orders):
 print(f'{i+1}. {order}')
# List comprehension — filter expensive items
prices = [100, 450, 30, 780, 220, 60]
expensive = [p for p in prices if p > 200]
print(expensive) # [450, 780, 220]
# Transform — apply 10% discount
discounted = [p * 0.90 for p in prices]
print(discounted) # [90.0, 405.0, 27.0, 702.0, 198.0, 54.0]
# while loop
inventory = ['item1', 'item2', 'item3']
while inventory:
 item = inventory.pop(0)
 print(f'Shipped: {item}')