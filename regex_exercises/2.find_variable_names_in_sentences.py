import re

sentence = input()
pattern = r"\b_([A-Za-z0-9]+)\b"
matches = re.findall(pattern, sentence)
print(",".join(matches))