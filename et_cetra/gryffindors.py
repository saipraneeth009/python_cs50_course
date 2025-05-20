students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

# gryffindors = [
#     student["name"] for student in students if student["house"] == "Gryffindor"
# ] 

# for gryffindor in sorted(gryffindors):
#     print(gryffindor)

## filter
# def is_gryffindor(s):
#     return s["house"] == "Gryffindor"

# gryffindors = filter(is_gryffindor, students)

# for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
#     print(gryffindor["name"])

## dict comprehensions

# students = ["Hermione", "harry", "Ron"]

# # gryffindors = []

# # for student in students:
# #     gryffindors.append({"name": student, "house": "Gryffindor"})

# # gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

# gryffindors ={student: "Gryffindor" for student in students}

# print(gryffindors)


students = ["Hermione", "harry", "Ron"]

# for student in students:
#     print(student)

# to get rank of each student
# for i in range(len(students)):
#     print(i+1, students[i])

# to get rank of each student using enumerate
for i, student in enumerate(students):
    print(i+1, student)