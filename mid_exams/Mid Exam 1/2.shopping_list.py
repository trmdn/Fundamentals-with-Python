initial_list = input().split("!")

while True:
    command = input()

    if command == "Go Shopping!":
        break

    current_command = command.split()
    command_part = current_command[0]

    if command_part == "Urgent":
        product = current_command[1]

        if product not in initial_list:
            initial_list.insert(0, product)

    elif command_part == "Unnecessary":
        product = current_command[1]
        if product in initial_list:
            initial_list.remove(product)

    elif command_part == "Correct":
        old_item, new_item = current_command[1], current_command[2]
        if old_item in initial_list:
            index = initial_list.index(old_item)
            initial_list[index] = new_item

    elif command_part == "Rearrange":
        product = current_command[1]
        if product in initial_list:
            initial_list.remove(product)
            initial_list.append(product)

print(", ".join(initial_list))
