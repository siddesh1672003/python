#wapp to get armstrong nos between 1 to 1000 with their count
cnt=0
print('Armstrong no.s between 1 to 1000 :')
for no in range(1,1000):
    no1 = no
    rev = 0
    while no>0:
        rem = no%10
        rev = rev+rem*rem*rem
        no = no//10
    if rev == no1:
        print(rev)
        cnt = cnt+1
print('Total count : ',cnt)