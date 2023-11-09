number_of_students = int(input())

students_dict = {}

for _ in range(number_of_students):
    name = input()
    grade = float(input())
    if name not in students_dict:
        students_dict[name] = {}
        students_dict[name][name + str(grade)] = 0
    if name in students_dict:
        students_dict[name][name + str(grade)] = 0
    students_dict[name][name + str(grade)] += grade

for name_student in students_dict:
    score = 0
    for key, value in students_dict[name_student].items():
        score += value
    avg_score = score / len(students_dict[name_student])
    if avg_score >= 4.50:
        print(f"{name_student} -> {avg_score:.2f}")