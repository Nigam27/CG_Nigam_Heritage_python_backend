entered_coupon = 'SAVE20' 

 

if (entered_coupon == 'WELCOME10' or 

    entered_coupon == 'SAVE20'    or 

    entered_coupon == 'FESTIVE50'): 

    print('Coupon applied successfully!') 

else: 

    print('Invalid coupon code.') 

# Output: Coupon applied successfully! 

 

# or with default value pattern 

user_city = None 

city = user_city or 'Kolkata'   # uses 'Kolkata' because user_city is falsy 

print(city)   # Kolkata 