main_string = input().split()
command = input()

def merge(start_index, end_index):
    if start_index < 0:
        start_index = 0
    if start_index < end_index:
        how_long = len(main_string)
        if end_index >= how_long:
            end_index = how_long - 1
        for num in range(start_index, end_index):
            main_string[start_index] += f"{main_string.pop(start_index + 1)}"

def divide(index, partitions):
    how_long = len(main_string[index])
    space_between = how_long // partitions
    string_to_change = main_string.pop(index)
    result = []
    for x in range(partitions - 1):
        result.append(string_to_change[:space_between])
        string_to_change = [string_to_change[space_between:]]
    result.append(string_to_change)
    for x in result[::-1]:
        main_string.insert(index, x)

while command != "3:1":
    command, start_index, end_index = [int(x) if x[-1].isdigit() else x for x in command.split()]
    if command == "merge":
        merge(start_index, end_index)
    elif command == "divide":
        divide(start_index, end_index)
    command = input()

print(" ".join(main_string))