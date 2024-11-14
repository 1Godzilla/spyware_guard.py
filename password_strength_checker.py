import re
import random
import string

def check_password_strength(password):
    print("Checking password strength...")  # Debug message to confirm function is called
    strength = 0
    feedback = []

    # Basic checks for password criteria
    if len(password) >= 12:
        strength += 1
    else:
        feedback.append("Password should be at least 12 characters long.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one number.")

    if re.search(r"[@$!%*?&]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character.")

    # Display strength and feedback
    if strength >= 4:
        print("Strong password!")
    else:
        print("Weak password.")
        for f in feedback:
            print(f)

def generate_strong_password():
    # Generate a strong password
    all_chars = string.ascii_letters + string.digits + "@$!%*?&"
    password = ''.join(random.choice(all_chars) for _ in range(12))
    return password

# Test the function
password = input("Enter a password to check its strength: ")
check_password_strength(password)

if __name__ == "_main_":
    print("\nSuggested strong password:", generate_strong_password())