class Bank:
    def __init__(self,accountHolder):
       self._balance = 0
       self._name = accountHolder

    def deposit(self,amount):
        if amount <= 0:
            return # Don't allow negative "deposits".
        self._balance += amount
        with open(self._name + 'Ledger.txt', 'a') as ledgerFile:
            ledgerFile.write('Deposit ' + str(amount) + '\n')
            ledgerFile.write('Balance is ' + str(self._balance) + '\n')

    def withdraw(self, amount):
         if self._balance < amount or amount < 0:
            return # Not enough in account, or withdraw is negative.
         self._balance -= amount
         with open(self._name + 'Ledger.txt', 'a') as ledgerFile:
            ledgerFile.write('Withdraw ' + str(amount) + '\n')
            ledgerFile.write('Balance is ' + str(self._balance) + '\n')