# def main():
#     yell("this is cs50")

# def yell(phrase):
#     print(phrase.upper())
    
# if __name__ == "__main__":
#     main()

# def main():
#     yell(["this", "is", "cs50"])

# def yell(words):
#     uppercased = []
#     for phrase in words:
#         # print(phrase.upper(), end =" ")
#         uppercased.append(phrase.upper())
#     print(*uppercased)
    
# if __name__ == "__main__":
#     main()

# def main():
#     yell("this", "is", "cs50")

# def yell(*words):
#     uppercased = []
#     for phrase in words:
#         uppercased.append(phrase.upper())
#     print(*uppercased)
    
# if __name__ == "__main__":
#     main()

## map
# def main():
#     yell("this", "is", "cs50")

# def yell(*words):
#     uppercased = map(str.upper, words)
#     print(*uppercased)
    
# if __name__ == "__main__":
#     main()

# list comprehension
def main():
    yell("this", "is", "cs50")

def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)
    
if __name__ == "__main__":
    main()