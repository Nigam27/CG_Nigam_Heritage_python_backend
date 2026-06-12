stored_username = 'admin' 

stored_password = 'SecurePass@123' 

 

entered_username = 'admin' 

entered_password = 'SecurePass@123' 

 

if entered_username == stored_username and entered_password == stored_password: 

    print('Login Successful! Welcome.') 

else: 

    print('Invalid credentials. Access Denied.') 

 

# != usage — check for duplicate email 

existing_email = 'user@example.com' 

new_email      = 'newuser@gmail.com' 

if new_email != existing_email: 

    print('Email available — registration allowed.') 

 