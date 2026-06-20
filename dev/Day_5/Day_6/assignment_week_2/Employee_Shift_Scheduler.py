shift = int(input("Enter shift number (1-3): "))

match shift:
    case 1:
        print("Morning Shift")
    case 2:
        print("Evening Shift")
    case 3:
        print("Night Shift")
    case _:
        print("Invalid Shift")