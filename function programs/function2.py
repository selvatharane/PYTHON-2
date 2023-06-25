'''Write a Python code with the function interest_calculation() which calculates the simple interest. The program should take the name of the customer, age of the customer, gender (‘M’ or ‘F’), principal amount (P), and number of years (N) as input.'''
def interest_calculation(p,n,r):
     si=(p*n*r)/100
     return si
name=input("enter name:")
age=int(input("age:")
g=input("gender:")
p=int(input("principa amount:"))
n=int(input("year:"))
temp=0
if(g=='F'):
   if(age<=60):
      temp=12
      res=interest_calculation(p,n,temp)
   else:
      temp=10
      res=interest_calculation(p,n,temp)
else:
     if(age<=60):
       temp=12
       res=interest_calculation(p,n,temp)
     else:
       temp=10
       res=interest_calculation(p,n,temp)
print(res)