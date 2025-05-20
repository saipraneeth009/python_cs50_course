## lists
# student = ["Hermione", "Harry", "Ron"]
# index 0: Hermione
# index 1: Harry
# index 2: Ron

# printing each index manually
# print(student[0])
# print(student[1])
# print(student[2])

# applying loop and printing
# for s in student:
#     print(s)

# adding range function
# for i in range(len(student)):
#     print(i+1, student[i])

## dicts

# students = {
#     "Hermione": "Griffindor",
#     "Harry": "Griffindor",
#     "Ron": "Griffindor",
#     "Draco": "Slytherin"
# }

# calling value based on key manually
# print("Draco:", students["Draco"])
# print("Harry:", students["Harry"])
# print("Hermione:", students["Hermione"])
# print("Ron:", students["Ron"])

# for looping
# for student in students:
#     print(student, students[student], sep = ": ")

# if there are more than 2 items
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}  # also can use "" instead of None.
]

for student in students:
    print(student["name"],student["house"],student["patronus"], sep = ": ")


