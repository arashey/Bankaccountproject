class Bankaccount:
    def __init__(self, owner, _id, balance):
        self.owner = owner
        self._id = _id
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print('enteghal byd bishtr az sefr bshd!')

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
            else:
                print('mojudi hesab kfi nist!')
        else:
            print('enteghal byd bishtr az sefr bshd!')

    def transfer(self, amount, target_account):
        if amount > 0:
            if amount <= self.balance:
                self.withdraw(amount)
                target_account.deposit(amount)
            else:
                print('mojudi hesab kfi nist!')
        else:
            print('enteghal byd bishtr az sefr bshd!')
class Savingaccount(Bankaccount):
    def __init__(self, owner, _id, balance, interest_rate):
        super().__init__(owner, _id, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        if self.interest_rate > 0:
            interest = self.balance * (self.interest_rate / 100)
            self.balance += interest
        else:
            print('sud byd dishtr az sefr bshd!')

b1 = Bankaccount(owner='eyvazkhani', _id=1204, balance=10000)
b2 = Savingaccount(owner='mohammadi', _id=3408, balance=0, interest_rate=5)

b1.transfer(5000, b2)
b2.add_interest()

print(f'{b1.balance} mojudi hesab {b1.owner}')
print(f'{b2.balance} mojudi hesab {b2.owner}')
