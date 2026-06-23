words = ["apple", "banana", "grape", "orange"]
target = "grape"

found_word = None

for word in words:
    if word == target:
        found_word = word
        break

if found_word is not None:
    print("Found word:", found_word)
else:
    print("Word not found")