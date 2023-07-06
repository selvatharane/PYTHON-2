'''Write a python program that has a list of positive and negative numbers.Make a new tuple that has only positive values from the list.
Sample Input: (-20,-4,-7,6,4,8,3,-6)
Sample Output: (6,4,8,3)'''
tuple=(-20,-4,6,4,8,3,-6)
tu1=()
for i in tuple:
    if(i>0):
        tu1+=(i,)
print(tu1)
