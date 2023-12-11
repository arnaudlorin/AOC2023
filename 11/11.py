# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 08:53:55 2023

@author: artan
"""


# set to 2 for part 1, set to 1000000 for part 2
shift=1000000-1
galaxie_list=[]
empty_row=0
notempty_col=set([])

f=open('input.txt')
for i,l in enumerate(f):
    l=l.split()[0]
    galaxie=[]
    for j,c in enumerate(l):
        if c=='#':
            galaxie.append([i+empty_row,j])
            notempty_col.add(j)
    if galaxie==[]:
        empty_row+=shift
    else:
        galaxie_list+=galaxie

col_all=set(range(len(l)))
empty_col=list(col_all-notempty_col)

col_all=[0]*(len(l))
for i in range(len(empty_col)):
    col_all[empty_col[i]]=1

icc=0
for i in range(len(col_all)):
    if col_all[i]==1:
        icc+=shift
    col_all[i]=icc
    

for i in galaxie_list:
    i[1]+=col_all[i[1]]

dist=0
for i in range(len(galaxie_list)):
    for j in range(i+1,len(galaxie_list)):
        dist+=abs(galaxie_list[i][0]-galaxie_list[j][0])+abs(galaxie_list[i][1]-galaxie_list[j][1])
        
print(dist)
