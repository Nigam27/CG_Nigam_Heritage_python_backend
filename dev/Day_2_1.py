
city = "Mumbai"

population = 20000000

country = "India"

# Multiple statements on one line — possible but not recommended

city = "Delhi"; population = 32000000; country = "India"

# Long statement split across multiple lines using backslash \

total = 100 + 200 + 300 + \
        400 + 500


# Better: use parentheses for line continuation (preferred way)

total = (
    100 + 200 + 300 +
    400 + 500
)

print(total)   # 1500