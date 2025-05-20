## In the terminal this .py file can be called in this way:
## python name.py <user-name>

import sys

# print("Hello, my name is", sys.argv[1])

# handling exception (error)
# try:
#     print("Hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")

# if len(sys.argv) < 2:
#     print("Too Few arguments")  # instead of print sys.exit can be used from sys module
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("Hello, my name is", sys.argv[1])

# if len(sys.argv) < 2:
#     sys.exit("Too Few arguments")  # instead of print sys.exit can be used from sys module
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")
# print("Hello, my name is", sys.argv[1])

## to add more than one argument

# if len(sys.argv) < 2:
#     sys.exit("Too few Arguments")

# for arg in sys.argv:
#     print("Hello, my name is", arg)

'''
output: python name.py praneeth sai meduri
Hello, my name is name.py
Hello, my name is praneeth
Hello, my name is sai
Hello, my name is meduri
'''

# in order to remove printing "name.py" statemt in results, we can use slices
if len(sys.argv) < 2:
    sys.exit("Too few Arguments")

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)