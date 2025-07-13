import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

user_input = input("Enter the desired password length: ")

if user_input.isdigit():
    user_length = int(user_input)
    result = generate_password(user_length)
    print("Generated Password:" if "Password" not in result else "", result)
else:
    print("Please enter a valid number.")
