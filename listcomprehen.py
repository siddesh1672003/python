'''syntax-
newList = [ expression(element) for element in oldList/range() if condition ] 
'''
#using list comprehension print even numbers
list=[x for x in range(101) if x%2==0]
print(list)

#matrix using list comprehension
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)