main_string = input()

result, show_result, number = "", "", "",

for index, symbols in enumerate(main_string):
    if not symbols.isdigit():
        result += symbols
    elif symbols.isdigit():
        number += symbols
        if index + 1 < len(main_string):
            if main_string[index + 1].isdigit():
                continue
        show_result += int(number) * result
        result, number = "", ""

show_result = show_result.upper()
print(f"Unique symbols used: {len(set(show_result))}")
print(show_result)
