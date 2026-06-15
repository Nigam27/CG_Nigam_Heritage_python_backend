item1_qty = int(input("Qty of Shirt (₹499 each): "))
item2_qty = int(input("Qty of Jeans (₹999 each): "))
discount_pc = float(input("Discount % (0 if none): "))
subtotal = (item1_qty * 499) + (item2_qty * 999)
discount = subtotal * (discount_pc / 100)
total = subtotal - discount
print(f"Subtotal : ₹{subtotal}")
print(f"Discount : ₹{discount:.2f}")
print(f"Total : ₹{total:.2f}")
