from datetime import date
# Basic: age in years
name = input("Enter your name : ")
year = int(input("Birth Year (YYYY) : "))
month = int(input("Birth Month (1-12) : "))
day = int(input("Birth Day (1-31) : "))
today = date.today()
dob = date(year, month, day)
age_days = (today - dob).days
age_yrs = age_days // 365
print(f"\n{name}, you are approximately {age_yrs} years old.")
