# Sorting numbers
prices = [299, 49, 799, 149, 499]
prices.sort() # ascending (default)
print(prices) # [49, 149, 299, 499, 799]
prices.sort(reverse=True) # descending
print(prices) # [799, 499, 299, 149, 49]
# Sorting strings
names = ['Charlie', 'Alice', 'Bob', 'Diana']
names.sort() # alphabetically
print(names) # ['Alice', 'Bob', 'Charlie', 'Diana']
# Sort by custom key — sort strings by length
words = ['banana', 'fig', 'apple', 'kiwi']
words.sort(key=len)
print(words) # ['fig', 'kiwi', 'apple', 'banana']
# sorted() returns a NEW list, doesn't modify original
original = [3, 1, 4, 1, 5]
new_sorted = sorted(original)
print(original) # [3, 1, 4, 1, 5] ← unchanged
print(new_sorted) # [1, 1, 3, 4, 5]