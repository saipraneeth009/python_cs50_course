## LOOPS

# to print a word n times

## dummy approach
# print("meow")
# print("meow")
# print("meow")

# print("meow\n" * 3, end ="")

## using while loop

# counting from 3 to 0 so that the loop gets satisfied
# i = 3
# while i != 0:
#     print("meow") # the loop continues infinitely
#     i -= 1 # by using this loop breaks after the value in i get to 0

# counting from 0 to 3 (to get 3 meow) 
# i = 0
# while i < 3:
#     print("meow")
#     i += 1

## using for loop

# example 1
# for i in [0, 1, 2]:
#     print("meow")

# example 2
# n = 0
# for i in range(4):
#     n +=1
#     print(f"{n}.meow")

# inplace of i, _ can be used
# n = 0
# for _ in range(4):
#     n +=1
#     print(f"{n}.meow")

##  take user desired input for number of times meow show happen:

# Approach with for loop, cant write infinite times
# n = int(input("how many times to meow: "))
# if n < 0:
#     n = int(input("how many times to meow(positive values only): "))
#     if n <0:

#Approach with while loop
# while True:
#     n = int(input("how many times to meow: "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")

# Approach for defining function for the above
def main():
    num = get_num()
    meow(num)
    
def get_num():
    while True:
        n = int(input("n: "))
        if n > 0:
            return n
        
def meow(n):
    for _ in range(n):
        print("meow")
        
main()