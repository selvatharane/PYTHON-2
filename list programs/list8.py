'''Write a python program to remove even numbers from the given list.
Sample Input:
[5,6,2,8,9,12,66]
Sample Output
[5,9] '''
a=list(map(int,input().split()))
l=[]
for list in a:
    if(list%2!=0):
        l.append(list)
print(l)
        
        
