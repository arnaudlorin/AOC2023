# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 08:02:45 2023

@author: artan
"""

redmax=12
greenmax=13
bluemax=14
count=0
f=open('input.txt')
for l in f:
    impossible=False
    l=l.split("\n")[0]
    idd=int(l.split(':')[0].split()[1])
    print(idd)
    color=l.split(':')[1].split(';')
    for i in color:
        for j in i.split(','):
            n=int(j.split()[0])
            col=j.split()[1]
            if (col=='red' and n>redmax) or (col=='green' and n>greenmax) or (col=='blue' and n>bluemax):
                impossible=True
                break
        if impossible:
            break
    if not impossible:
        count+=idd
        
print(count)