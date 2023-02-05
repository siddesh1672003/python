#wapp to show method overloading
class MO:
    def myFunction(self):
        print('Function with no argument')

    def myFunction(self,a):
        print('Function with one argument')
    
    def myFunction(self,a,b):
        print('Function with two argument')

m = MO()
m.myFunction(10,20)
#note : method overloading is not supported in python because it is an interpreted langauge