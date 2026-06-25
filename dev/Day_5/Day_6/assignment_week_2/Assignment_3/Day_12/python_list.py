import sys
import numpy as np

# Python List
my_list = [42, "hello", 3.14, True, [1, 2, 3]]

# Internal memory:
# A Python list stores references (pointers) to objects.
# [ptr -> 42] [ptr -> "hello"] [ptr -> 3.14] [ptr -> True] [ptr -> [1, 2, 3]]

numbers = [1, 2, 3, 4, 5]

# Size of the list object (includes overhead and pointers)
print("Size of Python list:", sys.getsizeof(numbers), "bytes")

# NumPy Array
np_arr = np.array([1, 2, 3, 4, 5], dtype=np.int32)

# Actual memory used by array elements
print("Size of NumPy array:", np_arr.nbytes, "bytes")