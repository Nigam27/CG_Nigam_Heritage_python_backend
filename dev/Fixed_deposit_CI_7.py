# Formula: A = P * (1 + r/n) ** (n*t) 

principal = 100000   # ₹1 lakh 

rate      = 0.07     # 7% annual 

n         = 4        # quarterly compounding 

years     = 5 

 

maturity = principal * (1 + rate/n) ** (n * years) 

print(f'Maturity Amount: ₹{maturity:.2f}')   # ₹141477.83 

 

# Squares and cubes 

side   = 6 

area   = side ** 2   # 36 

volume = side ** 3   # 216 