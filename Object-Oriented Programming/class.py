class library:
    def __init__(self):
        self.info = {}
        self.books = {}
        
    def add_info(self):
            while True:
                name = input("Name: ")
                if len(name) > 20:
                    print(f"Invalid")
                else:
                     print(f"{name}")
                     self.info["Name"] = name
                     break
        
            while True:
                phone = input("Phone #: ")
                if len(phone) != 11 or not phone.isdigit():
                     print("Invalid phone number.")
                else:
                     print(f"{phone}")
                     self.info["Phone #"] = phone
                     break
                
            print("\nDetails added successfully.")
            return self.info
    
    def add_books(self):
        while True:
              book = input("\nBook name -> Atomic Habits: ")
              if book != 'Atomic Habits':
                   print("Book name is wrong.")
              else:
                   print(f"{book}")
                   self.books["Book: "] = book
                   break
              
        while True:
              pages = int(input("Number of pages: "))
              if pages != 305:
                   print("Number of pages are 305.")
              else:
                   print(f"{pages}")
                   self.books["pages"] = pages
                   break
        print("\nBook Detail")
        return self.books
         
         
                
if __name__ == '__main__':
    find = library()
    print(find.add_info())
    print(find.add_books())