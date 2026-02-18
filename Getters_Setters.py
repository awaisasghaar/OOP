class Circle():
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self): # A getter to get the radius
        return self._radius
    
    @radius.setter
    def radius(self, value): # A setter to set the radius
        if value <= 0:
            raise ValueError('Value must be positive')
        self._radius = value
    
if __name__ == '__main__':
    # val = int(input("Enter the value: "))
    try:
       cal_circle = Circle(5)
       cal_circle.radius = 3
       print('Initial radius: ', cal_circle.radius)
       cal_circle.radius = 7
       print('Modified radius: ', cal_circle.radius)
       cal_circle.radius = 0
    except ValueError as e:
        print(f"{e}")