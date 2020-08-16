
'''c=65
for i in range(6,1,-1):
    ch=c
    for j in range(1,i):
        print(chr(ch),end="")
        ch=ch+1
    c=c+1
    print("\n")'''


ch=65
for i in range(1,6):
    for j in range(1,i+1,):
        print(chr(ch),end=" ")
    ch=ch+1
    print("\n")


'''ABCDE
BCDE
CDE
DE
E....'''
'''ch=65
for i in range(1,6):
    for j in range(i,6):
        print(chr(i),end=" ")
    ch=ch+1
    print("\n")'''
