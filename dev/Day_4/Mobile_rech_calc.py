# Program to calculate final recharge amount with GST

recharge_amount = float(input("Enter recharge amount: "))
gst_percentage = float(input("Enter GST percentage: "))

gst_amount = (recharge_amount * gst_percentage) / 100
final_amount = recharge_amount + gst_amount

print(f"Final payable amount: ₹{final_amount}")