# print("what is your name?")
# input_name = input()
# print("hello World")
# print(2+2)
# print("2"+"2") 

## ask user for their name
# name  = input("what is your name? ")
## say hello to the user
# print("hello " + name)
# print("hello", name)
# print("hello ", end="")
# print(name)

# print("hello, \"friend\"")

## f-string
# print(f"hello, {name}")

## remove white space from string
# name = name.strip() 

## capitalize first letter in the string
# name = name.capitalize() # if there is white space as first letterr it fails to keep capitalize 

## title
# name = name.title()

## remove whitespace from str and capitalize the first letter in string
# name = name.strip().title()

# name = input("what is your name: ").strip().title()

# ## split user name into first and last name
# fname, lname = name.split(" ")

# print(f"hello, {fname}")

# ********************************************************************************************* #
### USING FUNCTIONS (def)

# def hello(x = "world"):
#     print("hello,", x)

# name = input("user name: ")
# hello(name) #user defined function

def main():
    name = input("name: ")
    hello(name)
    
def hello(x = "world"):
    print("hello", x)
    
main()

