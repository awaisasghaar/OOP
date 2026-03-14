class Acount:
    def __init__(self, acount_1=0, acount_2=0, acount_3=0):
        self.acount_1 = acount_1
        self.acount_2 = acount_2
        self.acount_3 = acount_3
    
    def __str__(self):
        return f'{self.acount_1} PKR, ${self.acount_2}, {self.acount_3} Pound'
    
    def __add__(self, other):
        acount_1 = self.acount_1 + other.acount_1
        acount_2 = self.acount_2 + other.acount_2
        acount_3 = self.acount_3 + other.acount_3
        return Acount(acount_1, acount_2, acount_3)

if __name__ == '__main__':
    amount_1 = Acount(20000, 250, 150)
    print(f'\n','Acount 1 amount is ', amount_1)
    amount_2 = Acount(30000, 350, 250)
    print(f'Acount 2 amount is ', amount_2)
    
    total_amount = amount_1 + amount_2
    print(f'The total amount is ', total_amount)

# Output is

#  Acount 1 amount is  20000 PKR, $250, 150 Pound
# Acount 2 amount is  30000 PKR, $350, 250 Pound
# The total amount is  50000 PKR, $600, 400 Pound

        