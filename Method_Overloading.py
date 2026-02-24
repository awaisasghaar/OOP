class A:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def task(self, *args):
        result = 1
        for num in args:
            result *= num
        return result
    
if __name__ == '__main__':
   print('\nSimilar to Method overloading')
   
   val = A(a=2, b=3, c=4, d=5)
   answer = val.task(val.a, val.b, val.c, val.d)
   print('Result is', answer)


        