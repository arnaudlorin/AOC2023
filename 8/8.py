# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 09:31:48 2023

@author: artan
"""

class node:
    def __init__(self,label,left,right):
        self.label=label
        self.direction=[left,right]
        

f=open('input.txt')
sequence=f.readline().split()[0]
f.readline()
llabel=[]
ldirection=[[],[]]
for l in f:
    a=l.split('=')
    label=a[0][:-1]
    out=a[1]
    out=out.split('\n')[0].split(',')
    left=out[0][2:]
    right=out[1][1:-1]

    llabel.append(label)
    ldirection[0].append(left)
    ldirection[1].append(right)

n=len(sequence)
instructions=[0]*n
for i in range(len(sequence)):
    if sequence[i]=='L':
        instructions[i]=0
    else:
        instructions[i]=1
        
nlabel=len(llabel)
lnode=[0] * nlabel
for i in range(nlabel):
    lnode[i]=node(llabel[i],'','')
    if llabel[i]=='AAA':
        start=i

for i in range(nlabel):
    for j in range(nlabel):
        if llabel[j]==ldirection[0][i]:
            lnode[i].direction[0]=lnode[j]
            break
    for j in range(nlabel):
        if llabel[j]==ldirection[1][i]:
            lnode[i].direction[1]=lnode[j]
            break
    
cnode=lnode[start]
i=0
print(cnode.label)
while cnode.label!='ZZZ':
    cnode=cnode.direction[instructions[i%n]]
    i+=1
    print(cnode.label)
    
print(i)

""" Too long ! Too much loops !
i=0
pos=0   
label='AAA'

find=False
while label!='ZZZ':
    search=ldirection[instructions[i%n]][pos]
    for j,jlabel in enumerate(llabel):
        if jlabel==search:
            if jlabel=='ZZZ':
                find=True
            print(j,jlabel)
            i+=1
            pos=j
            label=jlabel
            break
#    if find:
#        break
print(i)

"""