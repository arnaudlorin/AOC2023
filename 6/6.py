# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 09:21:05 2023

@author: artan
"""

import math

ll=[]
f=open('input.txt')
for l in f:
    ll.append(l.split()[1:])
    
time=list(map(lambda x: int(x),ll[0]))
distance=list(map(lambda x: int(x),ll[1]))
nposs=1
for i in range(len(time)):
    delta=time[i]**2-4*(distance[i]+0.0001)
    if delta<0:
        print('No solution')
    else:
        t1=int((time[i]+delta**0.5)/2)
        t2=math.ceil((time[i]-delta**0.5)/2)
        nposs*=(t1-t2+1)
                
print(nposs)