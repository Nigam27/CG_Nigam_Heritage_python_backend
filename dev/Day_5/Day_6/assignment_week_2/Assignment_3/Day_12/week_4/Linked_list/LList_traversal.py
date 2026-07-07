def traverse(head):
 current = head # Start at the HEAD
 while current is not None:
    print(current.data, end=' → ') # Visit node
    current = current.next # Move forward
    print('None') # End of list
    # Usage:
    traverse(head)
    # Output: 10 → 20 → 30 → None