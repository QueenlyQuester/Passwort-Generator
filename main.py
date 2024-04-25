import secrets
import string


def generate_password(length: int) -> str:
    all_characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(all_characters) for _ in range(length))


while True:
    length_input = input("Enter the length of the password: ")
    if length_input.isdigit():
        length = int(length_input)
        break
    else:
        print(f"Invalid input: {length_input}. Please enter an integer.")

print(generate_password(length))
