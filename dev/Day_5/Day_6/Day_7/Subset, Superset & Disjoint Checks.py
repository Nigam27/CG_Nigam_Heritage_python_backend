admin_permissions = {'read', 'write', 'delete', 'admin', 'backup'}
user_permissions = {'read', 'write'}
guest_permissions = {'read'}
# issubset() — is every element of A in B?
print(user_permissions.issubset(admin_permissions)) # True
print(guest_permissions.issubset(user_permissions)) # True
# issuperset() — does A contain all elements of B?
print(admin_permissions.issuperset(user_permissions)) # True
# isdisjoint() — do A and B share NO elements?
special = {'audit', 'billing'}
print(user_permissions.isdisjoint(special)) # True (no overlap)
# Practical: check if user has required permissions
required = {'read', 'write'}
has_access = required.issubset(user_permissions)
print(f'Access granted: {has_access}') # Access granted: True