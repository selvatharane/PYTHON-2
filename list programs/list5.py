'''Write a python program which reads “n” words from the user, store it in the list and display the length of each word and display the longest word in the list.'''
string=list(input().split())
for i in string:
    print(len(i))
count=0
greatest=len(string[0])
for i in string:
    count+=1
    if(len(i)>greatest):
         greatest=len(i)
         a=count
print(string[a-1])
    









