# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 09:31:48 2023

@author: artan
"""

class node:
    def __init__(self,label,left,right):
        self.label=label
        self.direction=[left,right]
        
def prime(a):
    l=[]
    for i in range(2,a+1):
        if a==1:
            return l
        if a%i==0:
            icc=0
            while a%i==0:
                a=a//i
                icc+=1
            l.append([i,icc])
    return l
            
def lcm(l):
    decompo_prime=[]
    for i in range(len(l)):
        decompo_prime.append(prime(l[i]))
    print(decompo_prime)
    intersect=decompo_prime[0]
    for i in decompo_prime[1:]:
        for j in range(len(i)):
            present=False
            for k in range(len(intersect)):
                if i[j][0]==intersect[k][0]:
                    intersect[k][1]=max(intersect[k][1],i[j][1])
                    present=True
                    break
            if not present:
                intersect.append(i[j])
    icc=1
    for i in intersect:
        icc*=i[0]**i[1]
    return intersect,icc

            
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
for i in range(n):
    if sequence[i]=='L':
        instructions[i]=0
    else:
        instructions[i]=1
        
# Create the list of node and count number of starting and ending point
lstart=[]
nlabel=len(llabel)
lnode=[0] * nlabel
zlabel=[]
nz=0
for i in range(nlabel):
    lnode[i]=node(llabel[i],'','')
    if llabel[i][-1]=='A':
        lstart.append(i)
    elif llabel[i][-1]=='Z':
        nz+=1
        zlabel.append(llabel[i])

# Set up the references to the left and right node
for i in range(nlabel):
    for j in range(nlabel):
        if llabel[j]==ldirection[0][i]:
            lnode[i].direction[0]=lnode[j]
            break
    for j in range(nlabel):
        if llabel[j]==ldirection[1][i]:
            lnode[i].direction[1]=lnode[j]
            break

# Prepare the starting points
nghosts=len(lstart)
lcnode=[0] * nghosts
for i in range(nghosts):
    lcnode[i]=lnode[lstart[i]]
    
llz=[]
print('nstart=',nghosts)
print('nnodes=',nlabel)
for j in range(len(lcnode)):
    print(j)
    cnode=lcnode[j]
    start=lcnode[j].label
    i=0
    lz=[[] for _ in range(nz)]
    print('start',start)
    end=True
    while end:
        cnode=cnode.direction[instructions[i%n]]
        i+=1
        #print(cnode.label,lz)
        if cnode.label[-1]=='Z':
            for k in range(nz):
                if cnode.label==zlabel[k]:
                    break
            if len(lz[k])==1:
                if lz[k][0][1]==instructions[i%n]:
                    end=False
            elif len(lz[k])==2:
                end=False
            lz[k].append([i,instructions[i%n]])
            

    llz.append(lz)
lmini=[]
for i in llz:
    mini=10**12
    for j in i:
        if j==[]:
            continue
        mini=min(mini,j[0][0])
    lmini.append(mini)
print(lmini)
print(lcm(lmini))