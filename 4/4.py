# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 11:03:11 2023

@author: artan
"""

f=open('input.txt')
scoret=0
for l in f:
    l=l.split(':')[1].split('|')
    a=l[0].split()
    b=l[1].split()
    score=1
    for j in range(len(b)):
        b[j]=int(b[j])
    for i in a:
        i=int(i)
        for j in b: 
            if i==j:
                score*=2
    score=score//2
    scoret+=score
print(scoret)
        