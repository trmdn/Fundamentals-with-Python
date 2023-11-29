main_string = input()
command = input()

while command != "Reveal":
    command_type, *info = command.split(":|:")
    found_error = False
    if command_type == "ChangeAll":
        substring, changed_index = info
        main_string = main_string.replace(substring, changed_index)
    elif command_type == "Reverse":
        substring = info[0]
        if substring not in main_string:
            print("error")
            found_error = True
        else:
            word_find = main_string.find(substring)
            main_string = main_string[:word_find] + substring[::-1]
    elif command_type == "InsertSpace":
        index = int(info[0])
        main_string = main_string[:index] + " " + main_string[index:]

    if not found_error:
        print(main_string)

    command = input()

print(f"You have a new text message: {main_string}")