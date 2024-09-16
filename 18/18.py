# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 08:58:53 2023

@author: artan
"""

def inside(mat):
    ninside=0
    for i in range(len(mat)):
        ncross=0
        for j in range(len(mat[0])):
            if mat[i][j]=='|':
                #print(i,j,ncross)
                ncross=(ncross+1) % 2
            elif mat[i][j]=='F' or  mat[i][j]=='L':
                in_=mat[i][j]
            elif mat[i][j]=='7':
                if in_=='L':
                    ncross=(ncross+1) % 2
            elif mat[i][j]=='J':
                if in_=='F':
                    ncross=(ncross+1) % 2
            elif mat[i][j]=='.' and ncross==1:
                ninside+=1
            if mat[i][j]!='.':
                ninside+=1
    
    return ninside
    
    
list_pos=[]
pos=[0,0]
with open('inputex.txt') as f:
    for l in f:
        l=l.split()
        if l[0]=='L':
            i=0;j=-1
        elif l[0]=='R':
            i=0;j=1
        elif l[0]=='U':
            i=-1;j=0
        elif l[0]=='D':
            i=1;j=0
        for k in range(int(l[1])):
            pos[0]+=i
            pos[1]+=j
            list_pos.append([pos[0],pos[1]])
    
mini=0
maxi=0
minj=0
maxj=0
for i in list_pos:
    if mini>i[0]:
        mini=i[0]
    elif maxi<i[0]:
        maxi=i[0]
    if minj>i[1]:
        minj=i[1]
    elif maxj<i[1]:
        maxj=i[1]

print(list_pos)
print(mini,minj)
print(maxi,maxj)
mat=[ ['.' for _ in range(maxj-minj+1)] for i in range(maxi-mini+1)]
old_old_pos=list_pos[-2]
old_pos=list_pos[-1]
list_pos.append(list_pos[0])
for pos in list_pos:
    #old_pos=[list_pos[i-1][0]-mini,list_pos[i-1][1]-minj]
    #pos=[list_pos[i][0]-mini,list_pos[i][1]-minj]
    if pos[0]==old_old_pos[0]:
        car='-'
    elif pos[1]== old_old_pos[1]:
        car='|'
    elif pos[0]==old_pos[0]+1:
        if old_pos[1]==old_old_pos[1]+1:
            car='7'
        else:
            car='F'
    elif pos[0]==old_pos[0]-1:
        if old_pos[1]==old_old_pos[1]+1:
            car='J'
        else:
            car='L'
    elif pos[1]==old_pos[1]+1:
        if old_pos[0]==old_old_pos[0]+1:
            car='L'
        else:
            car='F'
    else:
        if old_pos[0]==old_old_pos[0]+1:
            car='J'
        else:
            car='7'
    #print()
    mat[old_pos[0]-mini][old_pos[1]-minj]=car
    old_old_pos=old_pos.copy()
    old_pos=pos.copy()

for i in mat:
    print(i)
print(mat[0])
print(inside(mat))