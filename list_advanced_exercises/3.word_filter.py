words = input().split()
filtered_word = [word for word in words if len(word) % 2 == 0]
print("\n".join(filtered_word))