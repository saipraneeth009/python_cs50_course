# _MEOWS = 3

# for _ in range(_MEOWS):
#     print("meow")

# class Cat:
#     MEOWS = 3
    
#     def meow(self):
#         for _ in range(Cat.MEOWS):
#             print("Meow")
            
# cat = Cat()
# cat.meow()

## for loop

# def meow(n: int):
#     for _ in range(n):
#         print("meow")

# number: int = int(input("Number:"))
# meow(number)

# def meow(n: int) -> None:
#     for  _ in range(n):
#         print("meow")

# number: int = int(input("Number:"))
# meows: str = meow(number)
# print(meows)
## output: mypy meows.py (mypy detected the error because of teh annotation of -> None)
# meows.py:22: error: Name "meows" is not defined  [name-defined]
# Found 1 error in 1 file (checked 1 source file)


# def meow(n: int) -> str:
#     """meow n times

#     Args:
#         n (int): number of times meows to be printed

#     Returns:
#         str: returns meow
#     """
#     return "Meow\n" * n

# number: int = int(input("Number:"))
# meows: str = meow(number)
# print(meows, end ="")


## adding sys.arg
# import sys

# if len(sys.argv) == 1:
#     print("meow")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("meow")
# else:
#     print("uaage: meows.py")

## argparse
import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="No. of times to meow", type=int)
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")