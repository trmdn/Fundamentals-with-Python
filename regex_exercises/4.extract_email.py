import re

find_email = input()

pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'

matches = re.findall(pattern, find_email, flags=re.IGNORECASE)

print("\n".join(matches))