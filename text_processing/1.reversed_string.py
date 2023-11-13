command = input()

while command != "end":
    text_reversed = ""
    for ch in reversed(command):
        text_reversed += ch
    print(command + "=" + text_reversed)

    command = input()