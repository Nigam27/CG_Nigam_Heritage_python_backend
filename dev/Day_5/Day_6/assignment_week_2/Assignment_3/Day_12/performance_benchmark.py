import time, numpy as np
 
SIZE = 1_000_000
 
# Python list addition
py_list = list(range(SIZE))
start = time.time()
result = [x * 2 for x in py_list]
print(f'Python list: {time.time() - start:.4f}s')
 
# NumPy array addition
np_arr = np.arange(SIZE)
start = time.time()
result = np_arr * 2
print(f'NumPy array: {time.time() - start:.4f}s')
 
# Typical output:
# Python list: 0.1200s
# NumPy array: 0.0015s   ← ~80x faster!
