# Program to check water intake target

glasses_consumed = int(input("Enter glasses consumed: "))
target_glasses = int(input("Enter target glasses: "))

target_achieved = glasses_consumed >= target_glasses

print(f"Target Achieved: {target_achieved}")