# list comprehension syntax

#newlist = [expression for item in iterable if condition == True]

#wapp to print a even list from 0-100 using list comprehension

lst = [i for i in range(101) if i%2==0] 
print(lst)