# ### int
# # x = 1
# # y = 2

# # x = input("x: ")
# # y = input("y: ")

# ## input as str -> int
# # x = int(x)
# # y = int(y)
# # z = int(x)+int(y)

# # x = int(input("what's x: "))
# # y = int(input("what's y: "))

# # z = x+y

# # print(z)
# # print(x + y)

# ## line comprehension
# # print(int(input("x: "))+int(input("y:")))

# ### float
# x = float(input('what is x: '))
# y = float(input('what is y: '))

# ## round the results to the whole number
# # z = round(x+y) # output: 1084 

# # print(z)
# ## adding commas as that of international numeric format
# # print(f"{z:,}") # output: 1,084

# ##division
# z = x/y
# # z = round(x/y, 2)


# # print(f"{z:.2f}") # .2f is the way of specifying how many digist after decimal must be printed
# print(f"{z:.3f}") # .3f is the way of specifying how many digist after decimal must be printed

# *************************************************************************************** #

### functions
def main():
    x = int(input("x: "))
    # y = int(input("y: "))
    print("x squared",square(x))
    
def square(n): 
    # return n * n
    # return n ** 2
    return pow(n, 4) # pow(number, raised power value)
main()
