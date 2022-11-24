import string
import random


def generate_password(length):
    characters = list(string.ascii_letters + string.digits)
    random.shuffle(characters)
    password = []
    for i in range(length):
        password.append(random.choice(characters))
    random.shuffle(password)
    return "".join(password)


def main():
    print(generate_password(12))

if __name__ == "__main__":
    main()