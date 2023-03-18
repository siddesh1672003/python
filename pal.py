#WAPP to check a no. is palindrome or not
n = int(input('Enter a no(3 digit no) : '))
rev = 0
n1 = n
a = n%10
n = n//10
b = n%10
n = n//10
c = n
rev = a*100+b*10+c

if rev == n1:
    print('No. is palindrome')
else:
    print('No. is not palindrome')
