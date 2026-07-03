queue = []

while True:
    print("\n1.Enqueue")
    print("2.Dequeue")
    print("3.Front")
    print("4.Display")
    print("5.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        item = int(input("Enter element: "))
        queue.append(item)

    elif choice == 2:
        if len(queue) == 0:
            print("Queue is Empty")
        else:
            print("Deleted:", queue.pop(0))

    elif choice == 3:
        if len(queue) == 0:
            print("Queue is Empty")
        else:
            print("Front:", queue[0])

    elif choice == 4:
        print(queue)

    elif choice == 5:
        break