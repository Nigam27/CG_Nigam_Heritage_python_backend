gross_income    = 800000 

standard_deduct = 50000 

hra_deduct      = 120000 

tax_rate        = 0.20 

 

# WRONG — missing parentheses causes wrong answer 

wrong_tax = gross_income - standard_deduct + hra_deduct * tax_rate 

# Evaluates as: 800000 - 50000 + (120000 * 0.20) 

#             = 800000 - 50000 + 24000 = 774000  ← WRONG! 

 

# CORRECT — parentheses enforce intended order 

taxable_income = gross_income - standard_deduct - hra_deduct 

correct_tax    = taxable_income * tax_rate 

print(f'Taxable Income : ₹{taxable_income}')   # ₹630000 

print(f'Tax Payable    : ₹{correct_tax}')       # ₹126000 

 