# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 09:20:17 2023

@author: artan
"""

rank=[]
lhand=[]
bid=[]
lforce=[]
f=open('input.txt')
for l in f:
    l=l.split()
    hand=[0]*13
    h=[]
    for j in l[0]:
        if j=='T':
            hand[8]+=1
            h.append(10)
        elif j=='J':
            hand[9]+=1
            h.append(11)
        elif j=='Q':
            hand[10]+=1
            h.append(12)
        elif j=='K':
            hand[11]+=1
            h.append(13)
        elif j=='A':
            hand[12]+=1
            h.append(14)
        else:
            hand[int(j)-2]+=1
            h.append(int(j))
    force=0
    for i in hand:
        if i==5:
            force=6
            break
        elif i==4:
            force=5
            break
        elif i==3:
            if force==1: # If a pair was already found --> House
                force=4
                break
            else:
                force=3
        elif i==2:
            if force==3: # If a three of a kind was already found --> House 
                force=4
                break
            elif force==1: # If a pair was already found --> Double pair
                force=2
                break
            else:
                force=1
    inserted=False
    found=False
    for i in range(len(lforce)):
        if force<lforce[i]:
            inserted=True
            break
        elif force==lforce[i]:
            for j in range(len(h)):
                if h[j]<lhand[i][j]:
                    inserted=True
                    break
                elif h[j]>lhand[i][j]:
                    break
            if inserted:
                break
    if not inserted:
        i+=1
    lforce.insert(i, force)
    lhand.insert(i,h)
    bid.insert(i,int(l[1]))
            
            
print(lforce)
print(lhand)
print(bid)

count=0
for i in range(len(bid)):
    count+=bid[i]*(i+1)
    
print(count)