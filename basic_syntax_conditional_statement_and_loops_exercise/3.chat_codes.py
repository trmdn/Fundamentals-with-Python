num_of_messages = int(input())

for i in range(num_of_messages):
    messages = int(input())

    if messages == 88:
        print("Hello")
    elif messages == 86:
        print("How are you?")
    elif messages < 88:
        print("GREAT!")
    elif messages > 88:
        print("Bye.")