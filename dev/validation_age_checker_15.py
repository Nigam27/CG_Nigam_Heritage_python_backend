age = 17 

 

if age >= 18: 

    print('Eligible to vote.') 

else: 

    print(f'Must be 18. You need {18 - age} more year(s).') 

 

# Retirement check 

retirement_age = 60 

current_age    = 58 

years_left     = retirement_age - current_age 

 

if current_age <= retirement_age: 

    print(f'{years_left} year(s) left until retirement.') 

 

# Speed limit checker 

speed_kmh = 85 

limit     = 80 

if speed_kmh > limit: 

    fine = (speed_kmh - limit) * 50 

    print(f'Speeding! Fine: ₹{fine}')