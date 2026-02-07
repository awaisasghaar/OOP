class Person:
    def __init__(self, name, age, gmail_id):
        self.name = name
        self.age = age
        self.gmail_id = gmail_id
    
    def student(self):
        print(f"{self.name} is {self.age}-years-old'")
    
    def study(self, gmail_id_2):
        self.gmail_id = gmail_id_2
        print(f"{self.name} has email address {gmail_id_2}")

# Creates the object of Person class and Call the method
a = Person("Awais", 22, "awaisasghaar13@gmail.com")
a.student()
a.study('awaisasghaar331@gmail.com')
