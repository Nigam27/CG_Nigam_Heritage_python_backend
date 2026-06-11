today_day_num = 2   # Wednesday 

days_from_now = 10 

 

future_day = (today_day_num + days_from_now) % 7 

days = ['Monday','Tuesday','Wednesday','Thursday', 

        'Friday','Saturday','Sunday'] 

print(f'Day after 10 days: {days[future_day]}')  # Saturday 

 

# Check even / odd 

number = 47 

if number % 2 == 0: 

    print('Even') 

else: 

    print('Odd')   # Output: Odd 