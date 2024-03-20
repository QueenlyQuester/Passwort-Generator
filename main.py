import secrets
import string
import sqlite3
import sys
from termcolor import colored
from passlib.hash import pbkdf2_sha256


def generate_password(length, use_digits=False, use_punctuation=False):
    characters = string.ascii_letters
    if use_digits or not use_punctuation:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation
    return "".join(secrets.choice(characters) for _ in range(length))


def get_user_input():
    while True:
        try:
            length = int(input("Enter password length (min 12 characters): "))
            if length < 12:
                raise ValueError("Password length must be at least 12 characters")
            break
        except ValueError as err:
            print(err)

    use_digits = input(f"Do you want to use digits (y/n): ").lower() == "y"
    use_punctuation = input(f"Do you want to use punctuation (y/n): ").lower() == "y"

    return length, use_digits, use_punctuation


def hash_password(password):
    return pbkdf2_sha256.hash(password)


def store_password_hash(password_hash, cursor, conn):
    try:
        cursor.execute(
            "INSERT INTO passwords (password_hash) VALUES (?);", (password_hash,)
        )
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error inserting password hash: {e}")
        sys.exit(1)


def main():
    try:
        conn = sqlite3.connect("passwords.db", detect_types=sqlite3.PARSE_DECLTYPES)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS passwords (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            password_hash TEXT NOT NULL UNIQUE);"""
        )
        length, use_digits, use_punctuation = get_user_input()
        password = generate_password(length, use_digits, use_punctuation)
        print(f"Generated password: {colored(password, 'green', 'on_grey')}")
        password_hash = hash_password(password)
        store_password_hash(password_hash, cursor, conn)
        print(f"Hashed password: {colored(password_hash, 'red', 'on_grey')}")
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
