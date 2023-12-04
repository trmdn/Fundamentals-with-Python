import re

def encrypt_password(password_input):
    pattern = re.compile(r'^(.+?)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|(.+?)<\1$')
    match = pattern.match(password_input)

    if match:
        encrypted_password = "".join(match.group(2, 3, 4, 5))
        print(f"Password: {encrypted_password}")
    else:
        print("Try another password!")


def main():
    number_of_passwords = int(input())

    for password in range(number_of_passwords):
        password_input = input("Enter the password: ")
        result = encrypt_password(password_input)
        print(result)


if __name__ == "__main__":
    pass