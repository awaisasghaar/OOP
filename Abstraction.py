# Data Abstraction
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    # Must be implement by subclass
    def student(self):
        pass

    # Concrete method which is shared by all
    def info(self):
        return f'My name {self.name} and {self.student()}'
    
class CS_student(Person):
    def student(self):
        return 'I am a Virtual University Student'

class grades(Person):
    def student(self):
        return 'I got 3.02/4.0 GPA'

# Only instantiate concrete subclass
print(CS_student('Awais').info())
print(grades('Awais').info())
