'''Write a program that generates a set of squares of numbers in the range(1-30) and another list generates numbers that are divisible by 3 in the range(1-30). Generate a newset from a
square set, which should not contain the numbers that are divisible by 3.'''
odd=set([i**2 for i in range(1,31)])
set1=set()
for i in range(1,31):
    if(i%3==0):
        set1.add(i)
print(odd-set1)
