'''Consider the given list and find the common elements of the three given lists USING SET.
List1 = [10, 45, 34, 20, 11]
List2 = [11, 25, 45, 20]
List3 = [20, 25, 11, 14, 45, 65]'''

list1 = [10, 45, 34, 20, 11]
list2 = [11, 25, 45, 20]
list3 = [20, 25, 11, 14, 45, 65]
set1=set(list1)
set2=set(list2)
set3=set(list3)
z=set1&set2
print(z&set3)
