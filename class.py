class Person:
    def __init__(self, name, age, degree):
        self.name = name
        self.age = age
        self.degree = degree
    
    def Student(self):
        return f"My name is {self.name} my age is {self.age} and my I''m pursuing {self.degree}"
    
student = Person('Awais', 22, 'Computer science')
print(student.name)
print(student.age)
print(student.degree)