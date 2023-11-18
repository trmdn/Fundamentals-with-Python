import re

text = "_ (Underscores) are also word characters!"
pattern = re.findall(r"\w+", text)
print(" ".join(pattern))
