# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 08:02:45 2023

@author: artan
"""

count=0
f=open('input.txt')
for l in f:
    rmax=0
    bmax=0
    gmax=0
    l=l.split("\n")[0]
    idd=int(l.split(':')[0].split()[1])
    print(idd)
    color=l.split(':')[1].split(';')
    for i in color:
        for j in i.split(','):
            n=int(j.split()[0])
            col=j.split()[1]
            if (col=='red' and n>rmax):
                rmax=n
            if (col=='green' and n>gmax):
                gmax=n
            if (col=='blue' and n>bmax):
                bmax=n
    print(rmax,gmax,bmax)
    count+=rmax*gmax*bmax
        
print(count)