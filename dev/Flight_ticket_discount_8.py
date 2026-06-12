age        = 68 

is_student = False 

is_senior  = age >= 60 

has_promo  = True 

 

# Senior OR student, AND has a promo code 

gets_discount = (is_senior or is_student) and has_promo 

print(f'Discount eligible: {gets_discount}')   # True 

 

# Complex real-world condition 

seat_available  = True 

payment_cleared = True 

passport_valid  = True 

 

can_board = seat_available and payment_cleared and not (not passport_valid) 

print(f'Boarding allowed: {can_board}')   # True