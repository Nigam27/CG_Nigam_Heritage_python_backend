cart_value = 2500 

 

if cart_value > 5000: 

    discount = 0.20   # 20% off 

elif cart_value > 2000: 

    discount = 0.10   # 10% off 

elif cart_value > 1000: 

    discount = 0.05   # 5% off 

else: 

    discount = 0.00 

 

savings    = cart_value * discount 

final_bill = cart_value - savings 

print(f'Discount: ₹{savings:.2f}, You Pay: ₹{final_bill:.2f}') 

# Output: Discount: ₹250.00, You Pay: ₹2250.00 