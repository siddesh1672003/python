#wapp to demonstrate a function without argu and without return 
def add():                              #function definition
    a = int(input('Enter 1st no : '))
    b = int(input('enter 2nd no : '))
    c = a+b
    print('Addition of two no.s : ',c)
add()                                   #function call

#wapp to show addition using a fun with argu and without return value
a = int(input('Enter 1st no : '))
b = int(input('Enter 2nd no : '))
def add(m,n):
    p = m+n
    print(p)

add(a,b)

#wapp to show addition of two no.s using function without argument and with return value
def add():
    a = 10
    b = 15
    return(a+b)
print(add())


#wapp to show addition using function with argu and with return
def add(m,n):
    o = m+n
    return o
print(add(19,45))
