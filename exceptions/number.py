## Exception Handling

# Approach 1
# try:
#     x = int(input("x: "))
# except ValueError:
#     print("x is not an integer, string and float are not accepted")
# else:
#     print(f"x is {x}")

# Approach 2: here asks user input until teh condition is satisfied
# while True:
#     try:
#         x = int(input("x: "))
#     except ValueError:
#         print("x is not an integer, string and float are not accepted")
#     else:
#         break

# print(f"x is {x}")

# Approach 3: no else used
# while True:
#     try:
#         x = int(input("x: "))
#         break
#     except ValueError:
#         print("x is not an integer, string and float are not accepted")

# print(f"x is {x}")

# Approach 4: defining function

def main():
    x = get_int("x: ")
    print(f"x is {x}")
    
def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            # print("x is not an integer, string and float are not accepted")
            pass # using pass instead of giving error

main()