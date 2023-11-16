strings = input()

show_result = ""
what_next = 0

for index in range(len(strings)):
    if what_next > 0 and strings[index] != ">":
        what_next -= 1
    elif strings[index] == ">":
        show_result += strings[index]
        what_next += int(strings[index + 1])
    else:
        show_result += strings[index]

print(show_result)