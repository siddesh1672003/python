#Wapp to check a number is prime or not
n = int(input('Enter a no : '))
cnt = 0
for i in range(1,n+1):
    if n%i==0:
        cnt= cnt+1
if cnt == 2:
    print('No is prime')
else:
    print('No is not prime')
