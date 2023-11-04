values = input().split(", ")
values_dict = {word: ord(word) for word in values}

print(values_dict)