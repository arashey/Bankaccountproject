class BankAccount:
    def __init__(self, owner, _id, balance):
        self.owner = owner
        self._id = _id
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("mablagh variz bayad bishtar az sefr bashad!")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("mojudi nakafi!")
        else:
            print("mablagh bardasht bayad bishtar az sefr bashad!")

    def transfer(self, target_account, amount):
        if amount > 0:
            if amount <= self.balance:
                self.withdraw(amount)
                target_account.deposit(amount)
            else:
                print("mojudi nakafi!")
        else:
            print("mablagh enteghali bayad kam tar az sefr bashad!")


ba1 = BankAccount(owner='eyvazkhani', _id=123,balance= 9000)
ba2 = BankAccount(owner='mohammadi', _id= 1234, balance=0)

ba1.transfer(ba2,1000)

print(f'{ba1.balance} mojudi hesab eyvazkhani')
print(f'{ba2.balance} mojudi hesab mohammadi')