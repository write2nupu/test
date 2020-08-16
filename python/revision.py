'''a=int(input("Enter your number"))
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")'''
'''a=1
b=2
print(a,b,end=" ")
for i in range(2,7):
    c=b+i
    print(c,end=" ")
    a=b
    b=c'''
'''a=1
print(a,end=" ")
for i in range(1,6):
    a=a+i*2
    print(a,end=" ")'''

n=int(input("Number"))
for num in range(1,n+1):
    if num>1:
        for r in range(2,num):
            if num%r==0:
                break
        else:
            print(num,end=" ")



