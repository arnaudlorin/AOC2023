# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 09:21:05 2023

@author: artan
"""

import math

ll=[]
f=open('input.txt')
for l in f:
    l=l.split('\n')[0].split(':')[1]
    acc=''
    for j in l:
        if j==' ':
            continue
        else:
            acc+=j
    ll.append(acc)

    
time=int(ll[0])
distance=int(ll[1])
nposs=1
for i in range(1):
    delta=time**2-4*(distance+0.0001)
    if delta<0:
        print('No solution')
    else:
        t1=int((time+delta**0.5)/2)
        t2=math.ceil((time-delta**0.5)/2)
        nposs*=(t1-t2+1)
                
print(nposs)