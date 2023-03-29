f = open("testfile1.txt","w+")
for i in range(10):
    f.write("This is line %d\r\n" %(i+1))
f.close()

f = open("testfile1.txt","a+")
for i in range(10):
    f.write("Appended line %d\r\n" %(i+1))
f = open("testfile1.txt","r")
str1 = f.read()
print(str1)

f.close()

