class Program():
    def __init__(self):
        # self.details = {'Awais': '+92-3006941108', 'Umair': '+92-3007632514'}
        self.info = {}
        
    # def search(self):
    #     while True:
    #           a = str(input('Name: '))
    #           if a in self.details:
    #               print(f"Name is {a} phone # is {self.details[a]}")
    #           else:
    #               print(f"{a} is not in dictionary")
    #               break

        # return self.details
    
    def add_info(self):
        # Name validation
        while True:
            name = input("Name: ")
            if len(name) < 3:
                print("Add at least 3 characters.")
            else:
                break

        # Phone validation
        while True:
            phone = input("Phone #: ")
            if not phone.isdigit():
                print("Digits only.")
            elif len(phone) != 11:
                print("Must be exactly 11 digits.")
            else:
                break

        self.info[name] = phone
        print(f"{name} added successfully.")
        return self.info
        
if __name__ == '__main__':
    find = Program()
    # find.search()
    find.add_info()
    print(find.add_info())
