'''Write a python program that scans an email address and forms a tuple of user name and domain
Sample Input:
22cs453@kpriet.ac.in
Sample output:
User name: 22cs452
Domain name: kpriet.ac.in'''
str=input()
name,domain=str.split('@')
print(name)
print(domain)
