<<<<<<< HEAD
# Real-world example: ATM PIN verification with nested conditions
balance = 15000
pin_correct = True
withdrawal_amount = 5000
 
if pin_correct:              # Level 1 — 0 spaces (inside if)
    print('PIN accepted')    # Level 1 — 4 spaces
    if withdrawal_amount <= balance:    # Level 2 — 4 spaces
        print('Processing...')         # Level 2 — 8 spaces
        balance = balance - withdrawal_amount
        print('New balance:', balance) # Level 2 — 8 spaces
    else:
        print('Insufficient funds')    # Level 2 — 8 spaces
else:
    print('Wrong PIN!')      # Level 1 — 4 spaces
=======
# Real-world example: ATM PIN verification with nested conditions
balance = 15000
pin_correct = True
withdrawal_amount = 5000
 
if pin_correct:              # Level 1 — 0 spaces (inside if)
    print('PIN accepted')    # Level 1 — 4 spaces
    if withdrawal_amount <= balance:    # Level 2 — 4 spaces
        print('Processing...')         # Level 2 — 8 spaces
        balance = balance - withdrawal_amount
        print('New balance:', balance) # Level 2 — 8 spaces
    else:
        print('Insufficient funds')    # Level 2 — 8 spaces
else:
    print('Wrong PIN!')      # Level 1 — 4 spaces
>>>>>>> c5bb30adadc4f31c27a6341fe84cf3fba09048c0
