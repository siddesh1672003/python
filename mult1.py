#wapp to show additiona nd multiplication of two nos using hiearchical inheritance
class NO:
    def get(self):
        self.a = int(input('Enter the 1st no : '))
        self.b = int(input('Enter the 2nd no : '))
class Add(NO):
    def add(self):
        self.c = self.a + self.b
        print('Addition : ',self.c)
class Mult(NO):
    def mult(self):
        self.c = self.a*self.b
        print('Multiplication : ',self.c)
a = Add()
a.get()
a.add()
m = Mult()
m.get()
m.mult()