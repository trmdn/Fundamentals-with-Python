import re

number_of_passwords = int(input())

for _ in range(number_of_passwords):
    password_input = input()
    pattern = re.compile(r'^(.+?)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|(.+?)<\1$')
    match = pattern.match(password_input)

    if match:
        encrypted_password = ''.join(match.group(2, 3, 4, 5))
        print(f"Password: {encrypted_password}")
    else:
        print("Try another password!")
