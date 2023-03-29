#reading and writing the file content

import pathlib


F1 = open("testfile1.txt","r")
if F1.mode == 'r':
    contents = F1.read()
print(contents)
print(F1.read(10))

#F1 = open("testfile1.txt","r")
print(F1.readline())
print(F1.readline(3))
print(F1.readlines())

F1.close()