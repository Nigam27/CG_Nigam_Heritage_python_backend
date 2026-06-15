# Login System with Role-Based Access

users_db = {
    'admin': {
        'password': 'admin@123',
        'role': 'admin',
        'active': True
    },
    'rahul': {
        'password': 'rahul2024',
        'role': 'user',
        'active': True
    },
    'priya': {
        'password': 'priya#321',
        'role': 'manager',
        'active': True
    },
    'blocked': {
        'password': 'pass',
        'role': 'user',
        'active': False
    },
}

def login(username, password):
    # Step 1: Check if username exists
    if username not in users_db:
        return 'ERROR', 'Username not found. Please register first.'

    user = users_db[username]

    # Step 2: Check if account is active
    if not user['active']:
        return 'BLOCKED', 'Account is disabled. Contact support.'

    # Step 3: Check password
    if user['password'] != password:
        return 'FAIL', 'Incorrect password. Please try again.'

    # Step 4: Grant access based on role
    role = user['role']

    match role:
        case 'admin':
            return 'OK', 'Admin access granted. Full control enabled.'

        case 'manager':
            return 'OK', 'Manager access granted. Reports & team access enabled.'

        case 'user':
            return 'OK', 'User access granted. Welcome!'

        case _:
            return 'OK', 'Access granted.'


# Simulate login attempts
tests = [
    ('admin', 'admin@123'),
    ('rahul', 'wrongpass'),
    ('unknown', 'any'),
    ('blocked', 'pass'),
    ('priya', 'priya#321'),
]

for uname, pwd in tests:
    status, msg = login(uname, pwd)

    icon = '✓' if status == 'OK' else '✗'

    print(f'{icon} [{uname}] -> {msg}')