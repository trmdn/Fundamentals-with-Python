def length(uname):
    if 3 <= len(uname) <= 16:
        return True
    return False


def characters(uname):
    for character in uname:
        if not character.isalnum() or character == "-" or character == "_":
            return False
        return True


def redundant_symbols(uname):
    if " " in uname:
        return False
    return True


def username_is_valid(uname):
    if length(uname) and characters(uname) and redundant_symbols(uname):
        return True
    return False


usernames = input().split(", ")
for username in usernames:
    if username_is_valid(username):
        print(username)