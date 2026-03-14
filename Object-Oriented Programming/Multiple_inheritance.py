# Parent class
class Person():
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs) # It will continue MRO chain
        self.name = name

    def intro(self):
        print(f"Hey, My name is {self.name}")

# Child class
class Student():
    def __init__(self, university, **kwargs):
        super().__init__(**kwargs)
        self.university = university
    
    def study(self):
        print(f"My Institution is {self.university} of Pakistan")

# Child class
class Student_2():
    def __init__(self, age, **kwargs):
        super().__init__(**kwargs)
        self.age = age
    
    def study_2(self):
        print(f"{self.age}")

# Inherits from all Person, Student, Student_2          
class info(Person, Student, Student_2):
    def __init__(self, name, university, age):
        super().__init__(name=name, university=university, age=age)

    def edu_info(self):
        print(f"{self.name} is at {self.university} and He is {self.age}")

if __name__ == '__main__':
#    my_intro = Person('Awais', 22, 'Computer Science', 'Virtual University')
   my_intro = info('Awais', 'Virtual University', '22-years-old')

   my_intro.intro() # Parent method
   my_intro.study() # Parent method
   my_intro.edu_info() # child method