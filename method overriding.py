#wapp to show method overridng
class MO1:
    def myFunction(self,a):
        print('Class MO1 function called')
        

class MO2(MO1):
    def myFunction(self,a):
        print('Class MO2 Function called')
        #Super method calling the method of class MO1
        super().myFunction(10)
    
class MO3(MO2):
    def myFunction(self,a):
        print('Class MO3 function called')
        # Super method calling the method of class MO2
        super().myFunction(10)

m = MO3()
m.myFunction(10)