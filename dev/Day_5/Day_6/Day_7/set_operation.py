# Subscribers to two newsletters
newsletter_A = {'Alice', 'Bob', 'Carol', 'David'}
newsletter_B = {'Carol', 'David', 'Eve', 'Frank'}
# UNION — all subscribers (from either)
all_subs = newsletter_A.union(newsletter_B)
# OR: newsletter_A | newsletter_B
print(all_subs)
# {'Alice', 'Bob', 'Carol', 'David', 'Eve', 'Frank'}
# INTERSECTION — subscribed to BOTH
both = newsletter_A.intersection(newsletter_B)
# OR: newsletter_A & newsletter_B
print(both) # {'Carol', 'David'}
# DIFFERENCE — only in A, not in B
only_A = newsletter_A.difference(newsletter_B)
# OR: newsletter_A - newsletter_B
print(only_A) # {'Alice', 'Bob'}
# SYMMETRIC DIFFERENCE — in one or the other, NOT both
exclusive = newsletter_A.symmetric_difference(newsletter_B)
# OR: newsletter_A ^ newsletter_B
print(exclusive) # {'Alice', 'Bob', 'Eve', 'Frank'}
