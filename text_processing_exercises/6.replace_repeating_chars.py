def remove_duplicates(input_str):
    result = ""
    previous_char = None

    for char in input_str:
        if char != previous_char:
            result += char
            previous_char = char
    return result


input_string = input()
final_result = remove_duplicates(input_string)
print(final_result)