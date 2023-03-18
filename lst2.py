#wapp to check whether a no is present in list
n = int(input('Enter a no : '))
lst = [10,20,30,40,50,60]
x = lst.count(n)
if x ==0 :
    print('No. is not presemt')
else:
    print('No. is present')