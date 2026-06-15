units = int(input('Enter units consumed: '))
if units <= 100:
    bill = units * 1.5
elif units <= 300:
    bill = 100 * 1.5 + (units - 100) * 3.0
elif units <= 500:
    bill = 100 * 1.5 + 200 * 3.0 + (units - 300) * 5.0
else:
    bill = 100 * 1.5 + 200 * 3.0 + 200 * 5.0 + (units - 500) * 7.0
print(f'Your electricity bill: Rs. {bill:.2f}')
