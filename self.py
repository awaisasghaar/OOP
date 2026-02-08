class Person:
    def __init__(self, name, field, CGPA):
        self.name = name
        self.field = field
        self.CGPA = CGPA
    
    def study(self, cgpa_increase):
        self.CGPA += cgpa_increase
        print(f"{self.name} CGPA has increased to {self.CGPA}")

my_cgpa = Person('Awais', 'Computer Science', 2.6)
my_cgpa.study(.3)

