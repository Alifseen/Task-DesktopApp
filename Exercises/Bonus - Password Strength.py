"""
check is a password is 8 characters or longer.
contains at least 1 digit
contains at least 1 capital letter
"""

password = input("Enter Password: ")
digit = False
upper = False


for char in password:
    if char.isupper():
        upper = True
    elif char.isnumeric():
        digit = True

if len(password) >= 8 and digit == True and upper == True:
    print("Strong Password")
else:
    print("Weak Password")
