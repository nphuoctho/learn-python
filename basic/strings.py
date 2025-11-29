"""
Project: Random Password Generator
"""

import random
import string

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation


def password_generator(length=8):
    printable = f"{LETTERS}{NUMBERS}{PUNCTUATION}"

    printable_list = list(printable)
    random.shuffle(printable_list)

    random_password = random.choices(printable_list, k=length)
    password = "".join(random_password)

    return password


def main():
    password_length = input("Enter the desired password length (default is 8): ")
    password = password_generator(
        int(password_length) if password_length.isdigit() else 8
    )
    print(f"Generated password: {password}")


if __name__ == "__main__":
    main()
