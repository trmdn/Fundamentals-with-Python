word = input()
count = int(input())

repeat_string = lambda a, b: a * b

result = repeat_string(word, count)
print(result)
