# Parent class: Person
class Person:
    def __init__(self, name, age, cgpa, subject):
        self.name = name
        self.age = age
        self.cgpa = cgpa
        self.subject = subject
    
    def intro(self):
        print(f'{self.name} is {self.age}-years-old and got {self.cgpa} cgpa')

# Child class
class Student(Person):
    def __init__(self, name, age, cgpa, subject, semester):

        # super function will call the parent class
        super().__init__(name, age, cgpa, subject) 
        self.semester = semester

    def study(self):
        print(f'He is a {self.subject} student and currently in {self.semester} semester')


if __name__ == '__main__' :
    my_intro = Student('\nAwais', 22, 2.8, 'Computer sciecne', '6th') # Object

    # Enter the input
    # a = input('Enter details: ')

    # # Using if and else statement
    # if a in ['Awais', 22, 2.8, 'Computer science']:
    #     print('\n Valid details')

    # else:
    #     print('Invlaid Details)


my_intro.intro() # Parent method
my_intro.study() # Child method
