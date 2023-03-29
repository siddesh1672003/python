fh = open("hello.txt","w")
lines_of_text = ["One line of text here","And another line here","and yet another line here","and so on hence forth"]

fh.writelines(lines_of_text)

fh.close()