## vertical lines

# print("#")
# print("#")
# print("#")

# for _ in range(3):
#     print("#")

# def main():
#     n = int(input("n: "))
#     print_column(n)
    
# def print_column(height):
#     # idea 1
#     # for _ in range(height):
#     #     print("#")
    
#     # idea 2
#     print("#\n" * height, end="")

# main()

# ## Horizontal Lines

# def main():
#     n = int(input("n: "))
#     print_row(n)
    
# def print_row(width):
#     # idea 1
#     # for _ in range(width):
#     #     print("?", end="")
    
#     # idea 2
#     print("?" * width, end="")

# main()

## creating a nxn square block

def main():
    n = int(input("n: "))
    print_square(n)

def print_square(size):
    # idea 1
    # # for each row in square
    # for i in range(size):
        
    #     # for each brick in row
    #     for j in range(size):
            
    #         # print brick
    #         print("#", end = "")
    #     # print("#")
    #     print()
    
    # idea 2 
    # for i in range(size):
    #     print("#" * size)
        

    # idea 3
    for i in range(size):
        print_row(size)
        
def print_row(width):
    print("#" * width)

main()