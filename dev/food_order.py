# Real-world example: Online food delivery order

# Creating variables (putting data in boxes)
customer_name = "Priya Sharma"
restaurant = "Biryani House"
order_total = 450.00
delivery_fee = 30.00
is_member = True
items_ordered = 3

# Using variables in calculations
gst = order_total * 0.05
final_amount = order_total + delivery_fee + gst

# Displaying the order receipt
print("========== ORDER RECEIPT ==========")
print("Customer:", customer_name)
print("Restaurant:", restaurant)
print("Items:", items_ordered)
print("Order Total: Rs.", order_total)
print("Delivery Fee: Rs.", delivery_fee)
print("GST (5%): Rs.", gst)
print("Final Amount: Rs.", final_amount)
print("Member Discount Applied:", is_member)
print("===================================")
