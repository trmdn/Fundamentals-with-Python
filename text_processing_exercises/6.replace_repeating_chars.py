text = input()
final_message = ""
last_added_message = ""
for current_char in text:
    if current_char != last_added_message:
        final_message += current_char
        last_added_message = current_char

print(final_message)