weight_kg = 70 

height_m  = 1.75 

bmi = weight_kg / (height_m ** 2) 

print(f'BMI: {bmi:.1f}')   # 22.9 

 

# Chained comparison — Python's elegant range check 

if   bmi < 18.5:              print('Underweight') 

elif 18.5 <= bmi < 25.0:     print('Normal weight')   # ← this fires 

elif 25.0 <= bmi < 30.0:     print('Overweight') 

else:                         print('Obese')