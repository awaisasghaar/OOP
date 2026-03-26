class library:
    def __init__(self):
        self.info = {}
        
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
                if phone.startswith('+92-'):
                     phone = '0' + phone[4:]
                if len(phone) != 11 or not phone.isdigit():
                     print("Invalid phone number.")
                else:
                     print(f"{phone}")
                     self.info["Phone #"] = phone
                     break
                
            print("\nDetails added successfully.")
            return self.info
                
if __name__ == '__main__':
    find = library()
    print(find.add_info())