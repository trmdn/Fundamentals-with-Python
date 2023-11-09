command = input()

school_info = {}

while command != "end":
    language, student = command.split(" : ")
    school_info[language] = school_info.get(language, {})
    school_info[language][student] = student
    command = input()

for lng in school_info:
    print(f"{lng}: {len(school_info[lng])}")
    for key, value in school_info[lng].items():
        print(f"-- {value}")