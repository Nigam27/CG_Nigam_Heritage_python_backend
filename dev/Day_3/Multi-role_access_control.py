is_admin   = False 

is_manager = True 

is_active  = True 

has_vpn    = False 

 

# Without parentheses — 'and' binds tighter than 'or' 

# Python reads it as: is_admin or (is_manager and is_active and has_vpn) 

access1 = is_admin or is_manager and is_active and has_vpn 

print(f'Access (no parens): {access1}')   # False 

 

# With parentheses — explicit intent 

access2 = (is_admin or is_manager) and is_active and has_vpn 

print(f'Access (with parens): {access2}')  # False (has_vpn blocks it) 

 

access3 = (is_admin or is_manager) and is_active 

print(f'Access (VPN optional): {access3}')  # True 