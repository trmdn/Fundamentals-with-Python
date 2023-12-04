followers = {}

while True:
    command = input()

    if command == "Log out":
        break

    tokens = command.split()

    if tokens[0] == "New":
        username = tokens[2]
        if username not in followers:
            followers[username] = {'likes': 0, 'comments': 0}

    elif tokens[0] == "Like:":
        username = tokens[1][:-1]
        count = int(tokens[2])
        if username not in followers:
            followers[username] = {'likes': count, 'comments': 0}
        else:
            followers[username]['likes'] += count

    elif tokens[0] == "Comment:":
        username = tokens[1]
        if username not in followers:
            followers[username] = {'likes': 0, 'comments': 1}
        else:
            followers[username]['comments'] += 1

    elif tokens[0] == "Blocked:":
        username = tokens[1]
        if username in followers:
            del followers[username]
        else:
            print(f"{username} doesn't exist.")

# Print the final result
print(f"{len(followers)} followers")
for username, stats in followers.items():
    print(f"{username}: {stats['likes'] + stats['comments']}")