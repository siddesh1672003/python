#wapp to print even and odd numbers in a range in a menu driven program

n = int(input('Enter starting position : '))
m = int(input('Enter end position : '))

c = input('Enter your choice : \n1.Even\n2.Odd \n')
if c == '1':
    print('Even numbers : ')
    for i in range(n,m+1):
        if i%2==0:
            print(i)
    
elif c == '2':
    print('Odd numbers : ')
    for i in range(n,m+1):
        if i%2!=0:
            print(i)
else :
    print('Invalid Choice')
