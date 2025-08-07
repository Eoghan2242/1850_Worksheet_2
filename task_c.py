password = input("Please enter your password: ")

if len(password) < 8:
    print("Your password must contain at least 8 characters, and a mix of letters and numbers")
else:
    letters = False
    numbers = False

    for char in password:
        if char.isalpha():  
            letters = True
        elif char.isdigit():  
            numbers = True

    if letters and numbers:
        print("Your password is valid")
    else:
        print("Your password must contain at least 8 characters, and a mix of letters and numbers")