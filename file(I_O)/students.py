# with open("students.csv") as file:
#     for line in file:
#         # row = line.rstrip().split(",")
#         # print(f"{row[0]} is in {row[1]}")
        
#         name, place = line.rstrip().split(",")
#         print(f"{name} is in {place}")

# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, place = line.rstrip().split(",")
#         students.append(f"{name} is in {place}")
        
# for student in sorted(students):
#     print(student)

## storing in dict

# with open("students.csv") as file:
#     for line in file:
#         name, place = line.rstrip().split(",")
#         student = {}
#         student["name"] = name
#         student["place"] = place
#         students.append(student)
        
# for student in students:
#     print(f"{student['name']} is in {student['place']}")

# with open("students.csv") as file:
#     for line in file:
#         name, place = line.rstrip().split(",")
#         student = {"name": name, "place": place}
#         students.append(student)
        
# # def get_name(student):
# #     return student["name"]

# def get_place(student):
#     return student["place"]

# for student in sorted(students, key=get_place , reverse=False):
#     print(f"{student['name']} is in {student['place']}")

## instead of write a function as get_name, get_place we can use lambda function
# with open("students.csv") as file:
#     for line in file:
#         name, place = line.rstrip().split(",")
#         student = {"name": name, "place": place}
#         students.append(student)


# for student in sorted(students, key=lambda student: student["name"] , reverse=False):
#     print(f"{student['name']} is in {student['place']}")

## using csv library
# import csv

# students = []

# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for name, home in reader:
#         students.append({"name": name, "home": home})

# for student in sorted(students, key=lambda student: student["name"] , reverse=False):
#     print(f"{student['name']} is from {student['home']}")


## if we have name, home in csv
# import csv

# students = []

# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})

# for student in sorted(students, key=lambda student: student["name"] , reverse=False):
#     print(f"{student['name']} is from {student['home']}")


## for writing into csv
# import csv

# name = input("name: ")
# home = input("home: ")

# with open("students.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])

import csv

name = input("name: ")
home = input("home: ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home":home})