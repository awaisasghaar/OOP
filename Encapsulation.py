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
    def __init__(self, balance):
        self.__balance = balance # Private attribute
    
    def deposit(self, amount): # Add to the balance safely
        if amount > 0:
            self.__balance += amount # Remove to the balance safely
    
    def withdraw(self, amount):
        if  amount > 0 and self.__balance >= 0:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance
    
if __name__ == '__main__':
    print('\nAccount no 1')
    account_1 = Account(500)
    account_1.deposit(200)
    print('Amount after deposit: ', account_1.get_balance())
    account_1.withdraw(100)
    print('Amount after withdraw: ', account_1.get_balance())
    
    print('\nAccount no 2')
    account_2 = Account(500)
    account_2.deposit(300)
    print('Amount after deposit: ', account_2.get_balance())
    account_2.withdraw(130)
    print('Amount after withdraw', account_2.get_balance())
    





    
