'''Write a python program which reads “n” number of integers from the user and generates a separate list containing even and odd numbers.'''
n=int(input("enter no of elements:"))
list=[]
i=1
while(i<=n):
    a=int(input())
    list.append(a)
    i+=1
c=[i for i in list if i%2==0]
print(c)
d=[i for i in list if i%2!=0]
print(d)

