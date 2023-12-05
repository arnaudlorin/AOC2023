# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 11:03:11 2023

@author: artan
"""

f=open('input.txt')
lscore=[]
for l in f:
    l=l.split(':')[1].split('|')
    a=l[0].split()
    b=l[1].split()
    score=0
    for j in range(len(b)):
        b[j]=int(b[j])
    for i in a:
        i=int(i)
        for j in b: 
            if i==j:
                score+=1
    lscore.append(score)
    
print(lscore)
nscratch=0
lscratch=[1]*len(lscore)
for i in range(len(lscore)):
    nscratch+=lscratch[i]
    for j in range(lscore[i]):
        lscratch[i+j+1]+=lscratch[i]
        
print(nscratch)
        