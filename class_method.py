class Employee:
    profile = None

    def __init__(self, name, role):
        self.name = name
        self.role = role
    
    def call(self):
        return f'Hey! my name is {self.name} I am {self.role}'
    
    @classmethod
    def portfolio(cls, project):
        cls.profile = project
        return cls.profile


if __name__ == '__main__':
# Creating the object
   emp_1 = Employee('Awais', 'Python Developer')
   
#    calls the classmethod
   emp_1.portfolio('Github Profile')
   print(emp_1.portfolio('Github Profile'))

#    calls the instance method 
   print(emp_1.call())

# Output below

# Github Profile
# Hey! my name is Awais I am Python Developer

