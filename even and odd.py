n=int(input('enter the size:'))
lst=[]
for j in range(n):
    element=int(input('enter the element:'))
    lst.append(element)
even=0
odd=0
for i in lst:
    if i%2==0:
        even +=1
    else:
        odd +=1
print('number of even numbers:',even)
print('number of odd numbers:',odd)
