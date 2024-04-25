import secrets
import string


def generate_password(length: int) -> str:
    all_characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(all_characters) for _ in range(length))


length_input = input("Enter the length of the password: ")

try:
    length = int(length_input)
except ValueError:
    print(f"Invalid input: {length_input}. Please enter an integer.")
    exit()

print(generate_password(length))
