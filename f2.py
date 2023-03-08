#wapp to check whether a string is palindrome

def pal(str):
    rev = []
    for i in range(len(str)):
        rev = str[::-1]
    if rev == str:
        print('palindrome')
    else:
        print('Not palindrome')
string = input('Enter a string : ')
lst = list(string)
pal(lst)
