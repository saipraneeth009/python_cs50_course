students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

## using for loop to remove duplicates

# houses = []
# for student in students:
#     if student["house"] not in houses:
#         houses.append(student["house"])
        
# for house in sorted(houses):
#     print(house)

## set
houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)