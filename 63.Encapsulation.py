class Account:
    def __init__(self,balance):
        self._balance=balance

    def get_balance(self):
        return self._balance

    def set_balance(self,balance):
        if balance>=0:
            self._balance=balance
        else:
            print("Balance cannot be negative.")

account=Account(1000)
print(account.get_balance())
account.set_balance(1500)
print(account.get_balance())