# EMI = [P * r * (1+r)^n] / [(1+r)^n - 1] 

# P = principal, r = monthly rate, n = tenure months 

 

P = 2000000   # ₹20 lakh loan 

annual_rate = 8.5 / 100 

r = annual_rate / 12           # monthly interest rate 

n = 20 * 12                    # 20 years = 240 months 

 

# Correct use of parentheses ensures proper precedence 

EMI = (P * r * (1 + r) ** n) / ((1 + r) ** n - 1) 

 

print(f'Monthly EMI: ₹{EMI:.2f}')   # ₹17,356.54 

print(f'Total Paid : ₹{EMI * n:.2f}') 

print(f'Interest   : ₹{(EMI * n) - P:.2f}') 