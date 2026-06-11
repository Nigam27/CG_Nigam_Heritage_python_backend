product_price = 1000.00 

inflation_rate = 1.08   # 8% increase per year 

 

product_price *= inflation_rate   # Year 1: ₹1080.00 

product_price *= inflation_rate   # Year 2: ₹1166.40 

product_price *= inflation_rate   # Year 3: ₹1259.71 

 

print(f'Price after 3 years: ₹{product_price:.2f}')   # ₹1259.71 