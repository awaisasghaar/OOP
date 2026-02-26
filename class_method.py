class Employee:
    resume = None

    def __init__(self, name, role):
        self.name = name
        self.role = role
    
    def call(self):
        return f'Hey! my name is {self.name} I am {self.role}'
    
    @classmethod
    def portfolio(cls, project):
        cls.resume = project
        return cls.resume


if __name__ == '__main__':
# Creating the object
   emp_1 = Employee('Awais', 'Python Developer')
   
#    calls the instance method 
   print(emp_1.call())
   
#    calls the classmethod
   emp_1.portfolio('Github Profile')
   print(emp_1.portfolio('Github Profile'))
