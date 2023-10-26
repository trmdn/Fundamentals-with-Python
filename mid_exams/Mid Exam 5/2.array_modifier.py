elements = [int(x) for x in input().split()]
data_info = input()

while data_info != "end":
    if "decrease" in data_info:
        elements = [x - 1 for x in elements]
        data_info = input()
        continue

    command, index_one, index_two = [x if x.isalpha() else int(x) for x in data_info.split()]

    if command == "swap":
        elements[index_one], elements[index_two] = elements[index_two], elements[index_one]

    elif command == "multiply":
        elements[index_one] *= elements[index_two]

    data_info = input()

print(*elements, sep=", ")
