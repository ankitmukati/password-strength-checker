import re


def check_password_strength(password):
    # Check length
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."

    # Check for lowercase
    if not re.search(r"[a-z]", password):
        return "Weak: Must include at least one lowercase letter."

    # Check for uppercase
    if not re.search(r"[A-Z]", password):
        return "Weak: Must include at least one uppercase letter."

    # Check for digit
    if not re.search(r"\d", password):
        return "Weak: Must include at least one digit."

    # Check for special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: Must include at least one special character."

    return "Strong Password ✅"


# ----------- MAIN PROGRAM ------------
user_password = input("Enter your password: ")
strength_result = check_password_strength(user_password)
print(strength_result)
