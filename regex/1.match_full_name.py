import re

name = input()

pattern = "\\b[A-Z][a-z]+ [A-Z][a-z]+\\b"
# pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
result = re.findall(pattern, name)

for name in result:
    print(name, end=" ")