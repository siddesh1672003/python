#wapp to print salary sheet using hiearchical inheritance
class Employee:
    def get(self):
        self.en = input('Enter the employee name : ')
        self.eno = int(input('Enter the employee no : '))
class Dept(Employee):
    def put(self):
        self.deptnm = input('Enter the employee department : ')
    def print(self):
        print(self.en,'\n',self.eno,'\n',self.deptnm)
class pay(Employee):
    def set(self):
        self.basic = int(input('Enter basic salary : '))
        self.da = self.basic*60//100
        self.hra = self.basic*10//100
    def printsal(self):
        print(self.basic,'\n',self.da,'\n',self.hra)
d = Dept()
d.get()
d.put()
p = pay()
p.set()
d.print()
p.printsal()