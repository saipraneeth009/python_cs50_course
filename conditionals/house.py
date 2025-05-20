## match statement
name = input("name: ")

## Approach 1
# if name == "Harry":
#     print("Gryffindor")
# elif name =="Hermoine":
#     print("Gryffindor")
# elif name == "Ron":
#     print("Griffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

## Approach 2
# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

## match

## approach 1
# match name:
#     case "Harry":
#         print("Griffindor")
#     case "Ron":
#         print("Griffindor")
#     case "Hermione":
#         print("Griffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("Who?")

## Approach 2
match name:
    case "Harry" | "Ron" | "Hermione":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")