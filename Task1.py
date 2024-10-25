import re

def check_length(password):
    """Check if the password length is sufficient."""
    return len(password) >= 8

def check_complexity(password):
    """Check for complexity: at least one lowercase, one uppercase, one digit, and one special character."""
    has_lower = re.search(r"[a-z]", password) is not None
    has_upper = re.search(r"[A-Z]", password) is not None
    has_digit = re.search(r"\d", password) is not None
    has_special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None
    return has_lower and has_upper and has_digit and has_special

def check_uniqueness(password):
    """Check if the password is not in a common password list."""
    common_passwords = set([
        "123456", "password", "123456789", "12345678", "12345",
        "1234567", "qwerty", "abc123", "football", "monkey",
        "letmein", "iloveyou", "admin", "welcome", "123123"
    ])
    return password not in common_passwords

def assess_password_strength(password):
    """Assess the strength of the given password."""
    length_ok = check_length(password)
    complexity_ok = check_complexity(password)
    uniqueness_ok = check_uniqueness(password)

    strength_score = sum([length_ok, complexity_ok, uniqueness_ok])
    
    if strength_score == 3:
        return "Strong"
    elif strength_score == 2:
        return "Moderate"
    else:
        return "Weak"

# Example usage
if __name__ == "__main__":
    user_password = input("Enter your password: ")
    strength = assess_password_strength(user_password)
    print(f"Password strength: {strength}")
