#wapp to check armstrong no 
n  = int(input('Enter a no : '))
n1 = n
rev = 0
while n>0:
    rem = n%10
    rev = rev+rem*rem*rem
    n = n//10
if rev == n1:
    print('No. is armstrong')
else:
    print('No. is not armstrong')