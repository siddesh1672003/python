#WAPP to demonstrate encapsulation by protected
class A:   #Parent Class 
    def __init__(self,a):
        self._a = a    #This is a protected variable
    def print(self):
        #printing a protected variable using function
        print('Private variable : ',self._a)

class B(A):  #Child Class
    def __init__(self,b):
        super().__init__(b)
    def showB(self):
        print('Variable value : ',self._a)

ob = B(45)
ob.showB()
    
