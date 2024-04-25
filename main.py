import secrets
import string

# Define a whitelist of allowed special characters
allowed_special_characters = "!@#$%^&*()-_=+[]{}|;:,.<>?/~`"


def generate_password(length: int) -> str:
    all_characters = string.ascii_letters + string.digits + allowed_special_characters
    return "".join(secrets.choice(all_characters) for _ in range(length))


def get_valid_length_input() -> int:
    while True:
        length_input = input(
            "Enter the length of the password (between 8 and 128 characters): "
        )
        try:
            length = int(length_input)
            if 8 <= length <= 128:
                return length
            else:
                print(
                    f"Invalid input: {length_input}. Please enter an integer between 8 and 128."
                )
        except ValueError:
            print(f"Invalid input: {length_input}. Please enter an integer.")


def check_password_strength(password: str) -> str:
    requirements = {
        "uppercase": any(c.isupper() for c in password),
        "lowercase": any(c.islower() for c in password),
        "digit": any(c.isdigit() for c in password),
        "special": any(c in allowed_special_characters for c in password),
    }
    num_requirements_met = sum(requirements.values())
    if num_requirements_met == 4:
        return "Strong"
    elif num_requirements_met == 3:
        return "Moderate"
    else:
        return "Weak"


length = get_valid_length_input()
password = generate_password(length)
strength = check_password_strength(password)
print(f"Generated password: {password}")
print(f"Password strength: {strength}")
