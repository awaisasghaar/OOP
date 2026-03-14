# Parent class
class Person():
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject
    
    def intro(self):
        print(f"His name is {self.name} age is {self.age} studying is "
              f"{self.subject}")

# Child class
class Student(Person):
    def __init__(self, name, age, subject, university):

        # Call parent constructor
        super().__init__(name, age , subject)
        self.university = university
    
    def study(self):
        print(f"{self.name} is at {self.university} studying {self.subject} "
              f" and age is {self.age}")

# Another child class            
class Cgpa(Student):
    def __init__(self, name, age, subject, university, cgpa):

        # Self mtehod
        super().__init__(name, age , subject, university)
        self.cgpa = cgpa
    
    def edu_info(self):
        print(f"{self.name} is at {self.university} studying {self.subject}"
        f" his age is {self.age} and {self.cgpa}")

if __name__ == '__main__':
   my_intro = Cgpa('Awais', 22, 'Computer science', 'Virtual University', 2.8)

   my_intro.intro() # Parent method
   my_intro.study() # Child method
   my_intro.edu_info() # child method