emp_name = "Priya Mehta"
department = "Software Engineering"
basic = 45000
hra = basic * 0.40
pf = basic * 0.12
gross = basic + hra
net = gross - pf
print(f"\n{"=" * 40}")
print(f" PAYSLIP — {emp_name}")
print(f" Dept: {department}")
print(f"{"=" * 40}")
print(f" Basic Salary : ₹{basic:>10,}")
print(f" HRA (40%) : ₹{hra:>10,.2f}")
print(f" PF (12%) : ₹{pf:>10,.2f}")
print(f"{"—" * 40}")
print(f" Gross Pay : ₹{gross:>10,}")
print(f" NET Pay : ₹{net:>10,.2f}")
print(f"{"=" * 40}")
