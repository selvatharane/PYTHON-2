'''Write a python program that reads integers from the user and stores them in a list. Your program should continue reading values until the user enters 0. Then it should display all of
the values entered by the user (except for the 0) in ascending order (The list itself to be sorted).'''
i=1
list=[]
while(i!=0):
    i=int(input())
    if(i!=0):
        list.append(i)
    else:
        break
list.sort()
print(list)
    
    
