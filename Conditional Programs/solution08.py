# Password checker

"""
Check if a password is "Weak", "Medium", or "Strong".
Criteria: <6 chars (Weak),
6-10 chars (Medium),
>10 chars (Strong).
"""

import re

def check_password_strength(password):
    """
    Determines the length of password based on its length and complexity.

    Parameters:
    password (str): The password to check.

    Returns:
    str: The strength of the password ("Weak", "Medium", or "Strong")
    """

    length_password = len(password)

    if length_password < 6:
        return "Weak"
    elif length_password <= 10:
        return "Medium"
    else:
        # Check for additional criteria for a strong password
        if (re.search(r"[a-zA-Z]", password) and
            re.search(r"[0-9]", password) and
            re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):
            return "Excellent"
        else:
            return "Strong"
        
def main():
    # Get password from user
    password = input("Enter password: ")

    # Determine the strength of the password
    strength = check_password_strength(password)

    print(strength)

if __name__ == "__main__":
    main()