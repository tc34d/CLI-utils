import random
import string

def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    pool = letters + digits + symbols
    password = ''.join(random.choice(pool) for i in range(length))
    return password

# Example usage
length = int(input("Enter the length of the password: "))
password = generate_password(length)
print("Your password is:", password)
