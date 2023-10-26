text = input().split()
words = ["Sand", "Water", "Fish", "Sun"]
print(sum([text.count(word) for word in words]))