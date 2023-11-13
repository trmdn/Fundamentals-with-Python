students_info = input()

student_dict = {}

while not student_dict.get(students_info):
    students_info = students_info.split(":")
    student_name = students_info[0]
    students_id = students_info[1]
    students_course = students_info[-1]
    if students_course not in student_dict:
        student_dict[students_course] = {}
    student_dict[students_course][student_name] = students_id
    students_info = input()
    students_info = students_info.replace("_", " ")

for key, value in student_dict[students_info].items():
    print(f"{key} - {value}")