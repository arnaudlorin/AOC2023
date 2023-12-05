# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 09:28:20 2023

@author: artan
"""


f=open("input.txt")
tot=0
for l in f:
    l=l.split()[0]
    print(l)
    for i in range(len(l)):
        if l[i].isnumeric():
            a=int(l[i])
            break
    for i in range(len(l)-1,-1,-1):
        if l[i].isnumeric():
            b=int(l[i])
            break
    print(a,b)
    tot+=10*a+b
print(tot)