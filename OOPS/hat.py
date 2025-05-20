## creating hat from that of harry potter that assigns the student to house

## simple implementation
# import random
# houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

# def sort(name):
#     print(name, "is in", random.choice(houses))
    
# sort("Harry")

## OOP implementation

# import random

# class Hat:
#     def __init__(self):
#         self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
        
#     def sort(self, name):
#         house = random.choice(self.houses)
#         print(name, "is in", house)


# hat = Hat()
# hat.sort("Harry")

## @classmethod
import random

class Hat:
    
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry")