# Real-world example: Simple loan eligibility checker
 
name = input("Enter your full name: ")
age_str = input("Enter your age: ")
salary_str = input("Enter your monthly salary (₹): ")
 
# Convert string input to numbers
age = int(age_str)          # Convert to integer
salary = float(salary_str)  # Convert to float
 
# Loan eligibility logic
min_age = 21
min_salary = 25000
 
print()
print("===== LOAN ELIGIBILITY RESULT =====")
print("Applicant:", name)
print("Age:", age)
print("Monthly Salary: ₹", salary)
 
if age >= min_age and salary >= min_salary:
    print("Status: ✅ ELIGIBLE for loan")
    max_loan = salary * 60
    print("Maximum Loan Amount: ₹", max_loan)
else:
    print("Status: ❌ NOT ELIGIBLE")
    print("Minimum age required: 21 years")
    print("Minimum salary required: ₹25,000/month")
