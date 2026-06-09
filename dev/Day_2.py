
balance = 15000


pin_correct = True

withdrawal_amount = 5000

if pin_correct:
    print("PIN accepted")
    
    if withdrawal_amount <= balance:
        print("Processing...")
        
        balance = balance - withdrawal_amount

        print("New balance:", balance)

    else:
        print("Insufficient funds")

else:
    print("Wrong PIN!")