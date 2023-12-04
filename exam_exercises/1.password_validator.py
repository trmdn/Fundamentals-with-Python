def is_valid_password(password):
    if len(password) < 8:
        print("Password must be at least 8 characters long!")
        return False
    if not all([char.isalnum() and char == '_' for char in password]):
        print("Password must consist only of letters, digits and _!")
        return False
    if not any([char.isupper() for char in password]):
        print("Password must consist at least one uppercase letter!")
        return False
    if not any([char.islower() for char in password]):
        print("Password must consist at least one lowercase letter!")
        return False
    if not any([char.isdigit() for char in password]):
        print("Password must consist at least one digit!")
        return False
    return True


def manipulate_password(password, command):
    if command.startswith("Make Upper"):
        index = int(command.split()[2])
        if 0 <= index < len(password):
            password = password[:index] + password[index].upper() + password[index:]
    elif command.startswith("Make Lower"):
        index = int(command.split()[2])
        if 0 <= index < len(password):
            password = password[:index] + password[index].lower() + password[index:]
    elif command.startswith("Insert"):
        _, index, char = command.split()
        index = int(index)
        if 0 <= index <= len(password):
            password = password[:index] + char + password[index + 1:]
    elif command.startswith("Replace"):
        _, char, value = command.split()
        if char in password:
            ascii_value = ord(char) + int(value)
            new_char = chr(ascii_value)
            password = password.replace(char, new_char, password.count(char))

    return password


password = input()
while True:
    command = input()

    if command == "Complete":
        break

    if not is_valid_password(password):
        break

    password = manipulate_password(password, command)
    print(password)
