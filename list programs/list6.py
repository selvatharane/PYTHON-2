'''A program should read “n” positive integers from the user and append it to the list, and if the list contains prime numbers return “True” and number of prime numbers, else “False”.'''
n=int(input())#count ofpositive integers
l=[]
a=[]
for i in range(n):
    b=int(input())
    l.append(b)
for i in l :
    count=1
    for j in range(2,i):#for checking whether the number is primre or not
        if(i%j==0):
            count=0 
            break
    if count==1:
        a.append(i)
if a!=[]:
    print("true")
    print(len(a))
else:
    print("false")





