import re

dates = input()
pattern = r'(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})'
result = re.finditer(pattern, dates)

for matches in result:
    days = matches.group(1)
    months = matches.group(3)
    years = matches.group(4)
    print(f'Day: {days}, Month: {months}, Year: {years}')