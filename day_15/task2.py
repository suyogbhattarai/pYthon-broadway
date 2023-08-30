# WAP to create a "login_required" decorator which if added to a function asks for a password. If the
# password is entered "123" then the function can be accessed else throw the message "Invalid Password"



@login_required
def addition(a, b):
    return a + b


result = addition(2, 3)
print(result)