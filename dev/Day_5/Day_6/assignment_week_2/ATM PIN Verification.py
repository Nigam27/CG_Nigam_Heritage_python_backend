correct_pin = "1234"
attempts = 3

while attempts > 0:
    pin = input("Enter PIN: ")

    if pin == correct_pin:
        print("Login Successful")
        break
    else:
        attempts -= 1
        print("Wrong PIN")
        print("Attempts left:", attempts)

if attempts == 0:
    print("Account Blocked")