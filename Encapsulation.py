# class Account:
#     def __init__(self, balance):
#         self._balance = balance # for internel use by convention
    
#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount # Add to the balance safely
    
#     def withdraw(self, amount):
#         if amount < 0:
#             self._balance -= amount # Remove the balance safely

class Account:
    def __init__(self):
        self.__balance = 0 # Private attribute
    
    def __validate(self, amount):
        if amount < 0:
            raise ValueError('Amount must be positive')
    
    def deposit(self, amount): # Add to the balance safely
        self.__validate(amount)
        self.__balance += amount
    
    def withdraw(self, amount): # Remove to the balance safely
        self.__validate(amount)
        if amount > self.__balance:
           raise ValueError('insufficient funds')
        self.__balance -= amount

    def get_balance(self):
        return self.__balance
    
if __name__ == '__main__':
    print('\nAccount no 1')
    account_1 = Account()
    print('Total amount: 0')
    account_1.deposit(200)
    print('Amount after deposit: ', account_1.get_balance())
    account_1.withdraw(100)
    account_1.withdraw(40)
    print('Amount after withdraw: ', account_1.get_balance())
    
    print('\nAccount no 2')
    account_2 = Account()

    # try/except
    try:
      print('Total amount: 0')
      account_2.deposit(-300)
    except ValueError as e:
      print(f"Deposit error: {e}")
      print('Amount after deposit: ', account_2.get_balance())
    
    try:
      account_2.withdraw(-130)
    except ValueError as e:
      print(f'Withdraw error: {e}')
      print('Amount after withdraw: ', account_2.get_balance())
    





    
