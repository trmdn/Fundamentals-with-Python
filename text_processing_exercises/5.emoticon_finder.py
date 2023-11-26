import re

message = input()

pattern = r"[:][)PO]"
result = re.findall(pattern, message)
print("\n".join(result))