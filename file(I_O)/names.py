## looping over names and saying hy to each name in teh list

# names = []

# for _ in range(3):
#     # name = input("name: ")
#     # names.append(name)
    
#     names.append(input("name: "))

# for name in sorted(names):
#     print(f"hello, {name}")

# ## storing in a file
# name = input("name: ")

# # file = open("names.txt", "a")
# # file.write(f"{name}\n")
# # file.close()

# ## instead of using close start the open with "with"

# with open("names1.txt", "a") as file:
#     file.write(f"{name}\n")

## to read the file

# with open("names.txt", "r") as file:
#     lines = file.readlines()
    
# for line in lines:
#     # print("hello, ", line, end ="")
#     print("hello, ", line.rstrip())

# with open("names.txt", "r") as file:
#     for line in sorted(file):
#         print("hello, ", line.rstrip())

# above can also be written as
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
        
for name in sorted(names, reverse=True):
    print(f"hello, {name}")
