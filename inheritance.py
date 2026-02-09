class Person:
    def __init__(self, name, age, cgpa, subject):
        self.name = name
        self.age = age
        self.cgpa = cgpa
        self.subject = subject
    
    def intro(self):
        print(f'{self.name} is {self.age}-years-old and got {self.cgpa} cgpa')

class Student(Person):
    def study(self):
        print(f'He is a {self.subject} student')

if __name__ == '__main__' :
    my_intro = Student('Awais', 22, 2.8, 'Computer sciecne')

    # Enter the input
    a = input('Enter details: ')

    # Using if and else statement
    if a in ['Awais', 22, 2.8, 'Computer science']:
        print('\n Valid details')
        my_intro.intro()
        my_intro.study()

    else:
        print('Invlaid Details.')

