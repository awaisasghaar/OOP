class library:
    def __init__(self):
        self.info = {}
        
    def add_info(self):
        while True:
            a = input("Name: ")
            if len(a) <= 15:
                print(f"{a}")
                break
            else:
                print(f"{a} is not valid")

            b = input("Phone #: ")
            if len(b) != 11:
                print(f"Invlaid input")
            else:
                print(f"{b}")
                break
        self.info = {"Name": a, "Phone #": b}
        return self.info

if __name__ == '__main__':
    find = library()
    find.add_info()