# first, last = input("name: ").split(" ")
# print(f"hello, {first}")

# def total(galleons, sickles, knuts):
#     return (galleons *17 + sickles) * 29 + knuts

# coins = [100, 50, 25]

# print(total(coins[0], coins[1], coins[2]), "Knuts")


## unpacking (*args, **kwargs)
"""
for list we use *args 
"""
# def total(galleons, sickles, knuts):
#     return (galleons *17 + sickles) * 29 + knuts

# coins = [100, 50, 25]

# print(total(*coins), "Knuts")

""" 
for dict we use **kwargs
"""
# def total(galleons, sickles, knuts):
#     return (galleons *17 + sickles) * 29 + knuts

# coins ={"galleons": 100, "sickles": 50, "knuts": 25}

# # print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")
# print(total(**coins), "Knuts")


def f(*args, **kwargs):
    # print("Positional: ", args)
    print("Named: ", kwargs)
    
# f(100, 50, 25)
f(galleons = 100, sickles = 50, knuts = 25)