class Employee:
    profile = '\nLinkedIn'

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

   print(Employee.profile)
   
#    calls the classmethod
   emp_1.portfolio('Github')
   print(emp_1.portfolio('Github'))

#    calls the instance method 
   print(emp_1.call())

# Output below

# LinkedIn
# Github 
# Hey! my name is Awais I am Python Developer

