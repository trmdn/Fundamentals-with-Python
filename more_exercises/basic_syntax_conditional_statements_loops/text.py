word = [x for x in input()]
list_of_upper = list()

for count, value in enumerate(word):
    if value.isupper():
        list_of_upper.append(count)
print(list_of_upper)
