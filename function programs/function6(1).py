'''Write a python program to display the answer for the following number series given the n value (Using Functions).
1/1! + 2/2! + 3/3! + ……. + n/n!
Sample Input
N = 6 (Number of terms)
Then the series will be 1/1! + 2/2! + 3/3! + 4/4! + 5/5! + 6/6!
Sample Output:
3.7159
Define a factorial function to calculate the denominator's value using recursion'''
def factorial(n):
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)
sum=0
for i in range(1,7):
    sum+=i/factorial(i)
print(sum)
