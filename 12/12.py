# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 08:25:01 2023

@author: artan
"""

def explore(l,ldam,ind):
    #print(ind,l,ldam)
    if ldam==[]:
        find=False
        for i in l:
            if '#' in i:
                find=True
                break
        if not find:
            return 1
        else: 
            return 0
    if l==[]:
        return 0
    to_insert=ldam[0]
    data=l[0]
    remain=l[1:]
    icc=0
    #first try to add a .
    if data[0]=='?':
        if len(data)==1:
            icc+=explore(remain,ldam,ind+'.  ')
        else:
            icc+=explore([data[1:]]+remain,ldam,ind+'. ')
    #print(ind,l,ldam)
    #Then try to add data #
    if len(data)<to_insert:
        icc+=0
    elif len(data)==to_insert:
        icc+=explore(remain,ldam[1:],ind+'  ')
    elif data[to_insert]=='?': # Have to add a dot at the end, check if possible
        if len(data)==to_insert+1:
            icc+=explore(remain,ldam[1:],ind+'  ')
        else:
            icc+=explore([data[to_insert+1:]]+remain,ldam[1:],ind+'  ')

    return icc
    
sum=0
f=open('input.txt')
for l in f:
    print()
    print(l)
    broken_input=l.split()[0]
    group=''
    lgroup=[]
    for i in broken_input:
        if i=='#' or i=='?':
            group+=i
        elif group!='':
            lgroup.append(group)
            group=''
    if group!='':
        lgroup.append(group)
    damaged=list(map(lambda x:int(x),l.split()[1].split(',')))

    sum+=explore(lgroup,damaged,'')

print(sum)