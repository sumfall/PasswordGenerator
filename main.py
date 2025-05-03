import random
import string
import secrets


def passw_gen(length: int = 32) -> str:
    if length < 4:
        # Instead of printing a warning and proceeding it puts up an error for an invalid input
        raise ValueError(
            "Password length must be at least 4 characters long for it to include all the required character types"
        )

    # Define the character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # makes sure that the password contains at least one of each type of character using secrets.choice
    password_chars = [
        secrets.choice(lowercase_letters),
        secrets.choice(uppercase_letters),
        secrets.choice(digits),
        secrets.choice(punctuation),
    ]

    all_characters = lowercase_letters + uppercase_letters + digits + punctuation

    # Do the rest of the password
    remaining_length = length - 4
    if remaining_length > 0:
        password_chars.extend(
            secrets.choice(all_characters) for _ in range(remaining_length)
        )
    random.SystemRandom().shuffle(password_chars)  # Use SystemRandom for shuffling

    # Put the list into a string
    return "".join(password_chars)


if __name__ == "__main__":
    # Generate a password using the default length of 32 characters
    generated_password = passw_gen()
    # Print the password
    print(
        f"Generated the {len(generated_password)} character long password: {generated_password}"
    )
