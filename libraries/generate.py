## generating code for coin flipping

# Random library

# 1. random.choice(seq)
# import random
# coin_flip = random.choice(["heads", "tails"])

# also can be written as 
# from random import choice
# coin_flip = choice(["heads", "tails"])

# print(coin_flip)

## generate random number in a range of numbers

# 2. random.randint(a, b)
# from random import randint

# num = randint(1, 20)
# print(num)

## shuffle items in list randomly

# 3. random.shuffle(x)
import random

cards = ["King", "Queen", "Jack"]
random.shuffle(cards)
for card in cards:
    print(card)