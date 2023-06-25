'''The python program should read the list of 5 numbers, and generate the new list which contains the factorial of each number in the given list. 
Sample Input
[2, 4, 8, 7, 5]
Sample Output
[2, 24, 40320, 5040, 120]'''
n=int(input("enter no of elements:"))
list=[]
i=1
while(i<=n):
    a=int(input())
    list.append(a)
    i+=1
list2=[]
b=1
for i in list:
    for j in range(1,i+1):
        b=b*j
    list2.append(b)
    b=1
print(list2)
