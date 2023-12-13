# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 09:13:26 2023

@author: artan
"""


def sub(l):
    li=[0]*(len(l)-1)
    for i in range(len(l)-1):
        li[i]=l[i+1]-l[i]
    return li

def exp(l,n):
    return(l[0]-n)

icc=0
f=open('input.txt')
for l in f:
    line=list(map(lambda x: int(x),l.split()))
    l=[]
    while True:
        allzero=True
        for i in line:
            if i!=0:
                allzero=False
        if allzero:
            l.append(line)
            break
        l.append(line)
        line=sub(line)
    n=0
    for i in range(len(l)):
        n=exp(l[len(l)-1-i],n)
    print(n)
    icc+=n
print(icc)