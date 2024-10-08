class BankAccount:
    def __init__(self, owner, _id, number_account, balance): 
        self.owner = owner
        self._id = _id
        self.number_account = number_account
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("mblgh variz byd bishtr az sefr bshd!")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("mojodi nkfi!")
        else:
            print("mblgh brdsht byd  az sefr bshd!")

    def transfer(self, target_account, amount):
        if amount > 0:
            if amount <= self.balance:
                self.withdraw(amount)
                target_account.deposit(amount)
            else:
                print("mojudi nakafi!")
        else:
            print("mblgh variz byd bishtr az sefr bshd!!")

correct_owner1 = "eyvazkhani"
correct_id1= 'a1204@'
correct_numberaccount2 = '60379972'
balance1= 90000000
balance2=0

while True: 
    owner1 = input("name khod ra vared  konid(:")
    if owner1 != correct_owner1:
        print('(name karbar eshtebah ast!)')
        continue
    
    id1 =(input("rmze obur ra vared konid:"))
    if id1 != correct_id1:
        print('(ramze obur eshtebah ast)')
        continue
    
    owner2 = input("name heasab mghsad ra vared konid:")
    number_account2 = input("shomare hesab mghsad ra vared konid:")
    if number_account2 != correct_numberaccount2:
        print('(shomare cart sahih nist!)')
        continue
    break

ba1 = BankAccount(owner=owner1, _id=id1,number_account=correct_numberaccount2 ,balance=balance1)
ba2 = BankAccount(owner=owner2,_id='67890' , number_account=number_account2, balance=balance2)

try:
    amount_to_transfer = float(input("lotfan mblagh morede nazar ra vared knid:"))
    ba1.transfer(ba2, amount_to_transfer)
except Exception as exe:
    print(f'lotfan add sahih vared konid {exe}')

print(f'{ba1.balance} mojudi hesab {owner1}')
print(f'{ba2.balance} mojudi hesab {owner2}')

