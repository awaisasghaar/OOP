class Person:
    def __init__(self, name, age, degree):
        self.name = name
        self.age = age
        self.degree = degree
    
student = Person('Awais', 22, 'Computer science')

print(f"Initial Attributes: {student.name} age is {student.age} and He is pursuing {student.degree}")
    
student.name = 'Umer'
student.age = 24
student.degree = 'Data science'

print(f"Modified attributes: {student.name} age is {student.age} and He is pursuing {student.degree}")