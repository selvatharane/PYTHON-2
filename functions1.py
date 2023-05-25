
def perfect(num):
    i=1
    while(num>=i):
        if(i**2==num):
            return("perfect square")
        i+=1
        
num=int(input())
result=perfect(num)
print(result)
