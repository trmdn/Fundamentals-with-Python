import string

usernames = input().split(", ")

for user in usernames:
    if 3 <= len(user) <= 16:
        for char in user:
            if char not in "-_" + string.ascii_letters + string.digits:
                break
        else:
            print(user)