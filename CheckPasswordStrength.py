def check_password_strength(password):
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return False

    lower = False
    upper = False
    digit = False
    special = False
    special_chars = "!@#$%^&*(),.?\":{}|<>"

    for char in password:
        if char.islower():
            lower = True
        if char.isupper():
            upper = True
        if char.isdigit():
            digit = True
        if char in special_chars:
            special = True

    if not lower:
        print("Password must have at least one lowercase letter.")
        return False
    if not upper:
        print("Password must have at least one uppercase letter.")
        return False
    if not digit:
        print("Password must have at least one digit.")
        return False
    if not special:
        print("Password must have at least one special character (!@#$...)")
        return False

    return True

# Ask the user
user_password = input("Enter your password: ")

if check_password_strength(user_password):
    print("Password Accepted!")
else:
    print("Sorry, retry. Password policy not met.")
