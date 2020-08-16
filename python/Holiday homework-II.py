'''lst = []

for i in range(100,401):
    A = 1
    for b in str(i):          
        if ord(b)%2 != 0:      
            A = 0          
    if A == 1:
        lst.append(str(i))

print(lst)'''

#begin
S=0
D=1000111
i=0
while D!=0:
    R=D%10
    S=S+R*2**i
    D=D//10
    i=i+1
    print("The Ascii number found is:",S)
    print("The equivalent character is:",chr(S))
    #ends
 
        
