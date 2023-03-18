#WApp to concatenate two strings using function

fnm = input('Enter first name : ')
lnm = input('Enter last name : ')
def add(a,b):
    return (a+b)
print(add(fnm,lnm))

#wapp to get last character of string usinf fun
str = input('Enter a string : ')
def lastchar(name):
    return name[-1]
print(lastchar(str))

#wapp to print list using fun

def show(lst):
    for i in lst:
        print(i)
lt = [1,2,3,4,5]
show(lt)