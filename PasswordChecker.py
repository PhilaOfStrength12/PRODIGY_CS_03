import re

def print_complexity(password: str):
    # Initialize flags for different character types
    has_lower = has_upper = has_digit = special_char = False

    # Define the set of normal characters (letters and digits)
    normal_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    # Calculate string length
    n = len(password)

    # Character type checking loop
    for char in password:
        if char.islower():
            has_lower = True
        if char.isupper():
            has_upper = True
        if char.isdigit():
            has_digit = True
        if re.search(r'\W', char):  # \W matches any non-word character
            special_char = True
    
    # Determine the strength of the password
    if n >= 8 and has_lower and has_upper and has_digit and special_char:
        strength = "Strong"
    elif n >= 6 and (has_lower or has_upper) and (has_digit or special_char):
        strength = "Moderate"
    else:
        strength = "Weak"

    # Outputting Password Strength
    print(f"Strength of password: {strength}")


def main():
    # User Input
    input_password = input("Enter your password: ")

    # Function Call
    print_complexity(input_password)

    # Return statement (not required in Python but used to match your C++ flow)
    return 0

if __name__ == "__main__":
    main()
