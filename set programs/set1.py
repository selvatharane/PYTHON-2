'''Write a program that generate a set of number that are prime numbers (1-50) and another set of numbers divisible by 5 (1-50),then apply union, intersection, difference and symmetric
difference on the resultant sets'''
c=1
odd=set()
for i in range(1,51):
    if(i%2!=0):
        odd.add(i)
set1=set()
for i in range(1,51):
    c=1
    for j in range(2,i):

        if(i%j==0):
            c=0
            break
    if(c==1):
        set1.add(i)
print(odd|set1)
print(odd&set1)
print(odd-set1)
print(odd^set1)
        

