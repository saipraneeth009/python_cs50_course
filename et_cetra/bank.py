## through global variable
# balance = 0

# def main():
#     print("Opening Balance:", balance)
#     deposit(100)
#     withdraw(50)
#     print("Closing Balance:", balance)
    
# def deposit(n):
#     global balance
#     balance += n

# def withdraw(n):
#     global balance
#     balance -= n
    
# if __name__ == "__main__":
#     main()

## oops
class Account:
    def __init__(self):
        self._balance = 0
    
    @property ## getter
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n
    
    def withdraw(self, n):
        self._balance -= n


def main():
    account = Account()
    print("Oepning Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Closing Balance:", account.balance)
    
if __name__ == "__main__":
    main()
    