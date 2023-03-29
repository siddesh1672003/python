fl1 = open("file1.txt","w")
fl1.write("I like Maths\n Not COA\n");

fl1 = open("file1.txt","r")
str = fl1.read(10);
print("Output string is : ",str)
fl1.close()
