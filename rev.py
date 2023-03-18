#WAPP to reverse a no. using while loop
n = int(input('Enter a no : '))
rev = 0
n1 = n
while n>0:
    rem = n%10
    rev = rev*10+rem
    n = n//10

print('Reverse of ',n1,' : ',rev)