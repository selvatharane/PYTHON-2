'''Write a Python function that takes base and power as arguments and calculates the power of numbers. 
Sample Input:
To Calculate 5 to the power of 3 then, enter the input as
Base : 5
Power : 3
Sample Output:
125'''
def power(base,power):
    c=base**power
    return c
s=power(5,3)
print("the power:",s)

