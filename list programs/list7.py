'''Write a python program that removes duplicates from the given list and generate the new list without duplicates.'''
l=[2,3,4,2,5,6,4,12,5]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)
