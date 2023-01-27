#WAPP to print factorial of a no,
n = int(input('Enter a no : '))
fact = 1
for i in range(1,n+1):
    fact = fact*i
print('Factorial of ',n,'=',fact)
