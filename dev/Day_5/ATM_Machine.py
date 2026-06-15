card_valid = True
pin_entered = 1234
correct_pin = 1234
balance = 5000
withdraw = 2000
if card_valid:
    if pin_entered == correct_pin:
        if withdraw <= balance:
            balance -= withdraw
            print(f'Rs.{withdraw} dispensed. Balance: Rs.{balance}')
        else:
            print('Insufficient balance')
    else:
        print('Incorrect PIN. Try again.')