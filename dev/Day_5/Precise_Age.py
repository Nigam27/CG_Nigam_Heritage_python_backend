from datetime import date
name = input("Name : ")
year = int(input("Birth Year (YYYY) : "))
month = int(input("Birth Month (1-12) : "))
day = int(input("Birth Day (1-31) : "))
dob = date(year, month, day)
today = date.today()
years = today.year - dob.year
months = today.month - dob.month
days = today.day - dob.day
if days < 0:
 months -= 1
 days += 30
if months < 0:
 years -= 1
 months += 12
total_days = (today - dob).days
total_weeks = total_days // 7
total_months = years * 12 + months
next_bday = date(today.year, dob.month, dob.day)
if next_bday < today:
 next_bday = date(today.year + 1, dob.month, dob.day)
days_to_bday = (next_bday - today).days
print(f"""
┌─────────────────────────────────────┐
│ AGE CERTIFICATE │
├─────────────────────────────────────┤
│ Name : {name:<21}│
│ Date of Birth : {str(dob):<21}│
│ Today : {str(today):<21}│
├─────────────────────────────────────┤
│ Age : {years} yrs, {months} months, {days} days │
│ Total : {total_days:,} days / {total_weeks:,} weeks │
│ Next Birthday in {days_to_bday} days │
└─────────────────────────────────────┘
""")