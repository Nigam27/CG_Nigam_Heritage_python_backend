# Real-world example: Employee Payslip Generator
employee = "Sneha Gupta"
basic_salary = 45000
allowances = 8000
deductions = 5500
net_salary = basic_salary + allowances - deductions
 
# METHOD 1: String Concatenation (OLD WAY — avoid)
print("Employee: " + employee + " | Net: " + str(net_salary))
# Ugly — need str() for numbers, + signs everywhere
 
# METHOD 2: .format() method (GOOD)
print("Employee: {}  |  Net Salary: ₹{}".format(employee, net_salary))
 
# METHOD 3: f-strings (BEST — modern Python 3.6+)
print(f"Employee: {employee}  |  Net Salary: ₹{net_salary}")
 
# f-strings can include expressions!
print(f"Basic: ₹{basic_salary:,}")
print(f"Allowances: ₹{allowances:,}")
print(f"Deductions: ₹{deductions:,}")
print(f"Net Salary: ₹{net_salary:,}")
print(f"Tax (10%): ₹{net_salary * 0.10:,.2f}")
