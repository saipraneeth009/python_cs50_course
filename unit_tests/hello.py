def main():
    name = input("name: ")
    print(hello(name))
    
def hello(x = "world"):
    return f"hello, {x}"

if __name__ == "__main__":
    main()

