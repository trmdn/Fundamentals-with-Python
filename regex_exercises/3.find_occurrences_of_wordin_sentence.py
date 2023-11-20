import re

text = input()
special_word = input()

pattern = r'\b{}\b'.format(re.escape(special_word))

matches = re.findall(pattern, text, flags=re.IGNORECASE)

print(len(matches))
