def valid_password(some_password: str) -> len:
    list_of_errors = []
    if len(some_password) < 6 or len(some_password) > 10:
        list_of_errors.append("Password must be between 6 and 10 characters")
    if not some_password.isalnum():
        list_of_errors.append("Password must consist only of letters and digits")
    digit_count = 0
    for character in some_password:
        if character.isdigit():
            digit_count += 1
    if digit_count < 2:
        list_of_errors.append("Password must have at least 2 digits")
    return list_of_errors


password = input()
errors_in_password = valid_password(password)
if not errors_in_password:
    print("Password is valid")
else:
    print("\n".join(valid_password(password)))
