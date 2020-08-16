list1=[]
count = int(input('please input total numbers--> '))
for i in range(count):
    number = int(input('Enter number: '))
    list1.append(number)
max = list1[0]
for x in list1:
    if x > max :
        max = x
print("maximum number in list->>>",max)
