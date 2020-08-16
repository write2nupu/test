'''a=0
b=1
print(a,b)
for i in range(1,21):
    s=a+b
    print(s)
    a=b
    b=s'''

'''sum=0
for i in range(1,11):
    num=int(input("Enter"))
    if num%2==0:
        sum=sum+num
    print(sum)'''

i=1
s=0
s1=0
n=int(input("Enter count"))
while i<=n:
    num=int(input("Enter no."))
    if num%2==0:
        s=s+num
    else:
        s1=s1+num
    i=i+1
print("Sum of even-",s)
print("Sum of odd-",s1)
