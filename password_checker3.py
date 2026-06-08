def check_password_strenth(password):
    score = 0
    suggestions = []
    

    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    if len(password) >=8:
        score +=1
    else:
        suggestions.append("use atleast 8 characters...")

    if has_lower:
        score +=1
    else:
        suggestions.append("add lowercase letters...")

    if has_upper:
        score +=1

    else:
        suggestions.append("add uppercase letters...")

    if has_digit:
        score +=1

    else: 
        suggestions.append("add numbers...")

    if has_special:
        score +=1

    else:
        suggestions.append("add special characters...")

    if "12345678" in password or "abcdefg" in password.lower() or "qwerty" in password.lower() or "password" in password.lower() or "admin" in password.lower():    
        score -= 2
        suggestions.append("Avoid predictable sequences like 12345678, abcdefg, or qwerty,or admin, or password or some common names.")

    if score <=2:
        strength = "weak"
    elif score <=4:
        strength = "medium"  
    else:
        strength = "strong"

    return strength, suggestions

import getpass

password = getpass.getpass("Enter your password: ")

while True:
    password = getpass.getpass("Enter your password: ")

    strength, suggestions = check_password_strenth(password)

    print("Password strength:", strength)

    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print("-", suggestion)

    again = input("\nCheck another password? yes/no: ").lower()

    if again != "yes":
        print("Goodbye!")
        break
    