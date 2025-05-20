## is this number even or odd
# x = int(input("x: "))

## Approach 1
# if x % 2 == 0:
#     print("even")
# else:
#     print("odd")

## Approach 2 (def)
def main():
    x = int(input("x: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False # it is not mandatory to add this statement but does same if not written

## line comprehension
## 1
# def is_even(n):
#     return True if n % 2 == 0 else False

## 2
def is_even(n):
    return n % 2 == 0 # or can be used this (n % 2 == 0)

main()
