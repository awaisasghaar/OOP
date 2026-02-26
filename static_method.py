class Employee:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary
    
    def profile(self):
        return f'Name: {self.name} Role: {self.role} Salary: '\
        f'{self.salary} (PKR)'
    
    @staticmethod
    def cal(salary):
        salary *= 2.4
        return f'Salary After 2-years {salary:.0f} (PKR)'

    
if __name__ == '__main__':
    emp_1 = Employee('Awais', 'Python Developer', 20000)
    print(emp_1.profile())
    print('Salary before: ', emp_1.salary, '(PKR)')
    print(emp_1.cal(emp_1.salary))

# Output below

# Name: Awais Role: Python Developer Salary: 20000 (PKR)
# Salary before:  20000 (PKR)
# Salary After 2-years 48000 (PKR)