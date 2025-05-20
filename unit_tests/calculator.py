def main():
    # x = int(input("x: "))
    x = input("x: ") ## instead of int it just takes in string
    print("x squared",square(x))


def square(n): 
    # return n * 2
    return n**2
    # return n+n


if __name__ == "__main__":
    main()