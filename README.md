# OOP
Object Oriented Programming using Python

# Introduction to Classes

Imagine you are a student trying to store information by individual variables

name = 'Awais'
age = 22
education = 'BS Computer Science'

name = 'Umer'
age = 24
education = 'BS Data Science'

This approach has a few problems:

1. Repetition: You have to define each hero individually.
2. Messy code: It's hard to keep track of all the hero attributes and their values.
3. Scalability: What if you need to create 50 different heroes? Your code would become unmanageable very quickly.

A class is a blueprint for creating objects. 

# Here is the basic syntax for defining a class in Python:

class Person:
    def __init__(self, name, age, degree):
        self.name = name
        self.age = age
        self.degree = degree

In Python, a class is defined with the keyword word class followed by the name of the class and a colon. The __init__ method is a special method that belongs to the class. It creates an object and initializes it's attributes.

Notice that the __init__ method has an argument self. This is required. The self variable allows us to add attributes to our object. It also prevents name conflicts, since name and self.name are different variables.

