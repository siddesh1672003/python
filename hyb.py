#WAPP to print salary sheet
class Employee:
    def get(self):
        self.en = input('Enter the name of employee : ')
        self.no = int(input('Enter the no of employee : '))

class Dept(Employee):
    def input(self):
        self.deptnm = input('Enter the department of employee : ')
class Job:
    def put(self):
        self.desig = input('Enter the designation : ')
class Pay(Dept,Job):
    def calc(self):
        self.basic = int(input('Enter the basic salary : '))
        self.da = self.basic*60//100
        self.hra = self.basic*10//100
        print(self.en,'\n',self.no,'\n',self.deptnm,'\n',self.basic,'\n',self.da,'\n',self.hra,'\n',self.desig)

e = Pay()
e.get()
e.input()
e.put()
e.calc()