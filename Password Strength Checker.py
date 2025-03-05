import re

def password_strength(password):
    strength = 0
    feedback = []

    # Check length
    if len(password) < 8:
        feedback.append("Password is too short. Should be at least 8 characters long.")
    else:
        strength += 1

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for digits
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Check for special characters
    if re.search(r'[@$!%*?&#«»{}—¿¡‽≠¬±~≈÷π†‡€$¥¢£ß™©®@½²]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Feedback based on strength score
    if strength == 5:
        feedback.append("Your password is strong.")
    elif strength >= 3:
        feedback.append("Your password is moderate.")
    else:
        feedback.append("Your password is weak.")

    return feedback

# Example usage
password = input("Enter your password: ")
result = password_strength(password)
for line in result:
    print(line)
