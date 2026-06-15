# Professional Bank Statement Output
name = "Arjun Sharma"
acc_no = "SBI00987654"
balance = 87432.60
transactions = [
 ("Salary Credit", "+₹50000"),
 ("Rent Debit", "-₹12000"),
 ("Grocery Debit", "-₹3200"),
]
print("=" * 45)
print(f" Account Holder : {name}")
print(f" Account Number : {acc_no}")
print(f" Balance : ₹{balance:,.2f}")
print("=" * 45)
print(f" {"Description":<25} {"Amount":>10}")
print("-" * 45)
for desc, amt in transactions:
 print(f" {desc:<25} {amt:>10}")
print("=" * 45)
