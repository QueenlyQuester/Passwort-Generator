import secrets
import string


def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(all_characters) for i in range(length))
    return password


length = int(input("Enter the length of the password: "))
print(generate_password(length))
