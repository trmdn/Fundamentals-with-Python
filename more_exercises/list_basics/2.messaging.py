numbers = [x for x in input().split()]
text = input()

msg_show = ""

for num in numbers:
    find_index = sum([int(s_num) for s_num in num])
    if find_index >= len(text):
        find_index -= len(text)
    msg_show += text[find_index]
    text = text[:find_index] + text[find_index + 1:]
print(msg_show)