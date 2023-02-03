 #WAPP to demonstrate encapsulation by private 
class A:   #Parent Class 
    def __init__(self,a):
        self__a = a    #This is a protected variable
    def print(self):
        #printing a private variable using function
        print('Private variable : ',self._a)

class B(A):  #Child Class
    def __init__(self,b):
        super().__init__(b)
    def showB(self):
        print(self.__a)

ob = B(45)
ob.showB()
    
        
