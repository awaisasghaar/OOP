class Circle():
    def __init__(self, radius):
        self._radius = radius # Private attribute
    
    # Getter
    @property
    def radius(self): # A getter to get the radius
        return self._radius
    
    # Setter
    @radius.setter
    def radius(self, value): # A setter to set the radius
        if value <= 0:
            raise ValueError('Value must be positive')
        self._radius = value
    
    # Deleter
    @radius.deleter
    def radius(self): # A deleter to delete the radius
        print("Deleting radius")
        del self._radius

    
if __name__ == '__main__':
    # val = int(input("Enter the value: "))
       # Create circle object with radius
       cal_circle = Circle(5)
       print(cal_circle.radius)

       # Delete the radius
       # This calls the deleter
       del cal_circle.radius 
       print('Radius deleted ')

    #    cal_circle.radius = 7
    #    print('Modified radius: ', cal_circle.radius)
    #    cal_circle.radius = 0
       try:
           print(cal_circle.radius)
       except AttributeError as e:
           print(f"OOPS! {e}")