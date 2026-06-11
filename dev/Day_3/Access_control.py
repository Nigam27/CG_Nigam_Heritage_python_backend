is_admin   = False 

is_blocked = True 

 

if not is_admin: 

    print('Access Denied — Admin only area.') 

 

if not is_blocked: 

    print('User is active.') 

else: 

    print('Account is suspended.') 

 

# Toggle a flag 

dark_mode = True 

dark_mode = not dark_mode   # Switch to False 

print(f'Dark mode: {dark_mode}')   # False 