# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 09:07:51 2023

@author: artan
"""

# overflow...
def explore_rec(mat,l,p,pre_p):
    oldp=[p[0],p[1]]
    pipe=mat[p[0]][p[1]]
    pre_pipe=mat[pre_p[0]][pre_p[1]]
    print(p,pipe)
    if pipe=='|':
        if pre_p[0]==p[0]-1:
            p[0]+=1
        else:
            p[0]-=1
    elif pipe=='-':
        if pre_p[1]==p[1]-1:
            p[1]+=1
        else:
            p[1]-=1
    elif pipe=='L':
        if pre_p[0]==p[0]-1:
            p[1]+=1
        else:
            p[0]-=1
    elif pipe=='J':
        if pre_p[1]==p[1]-1:
            p[0]-=1
        else:
            p[1]-=1
    elif pipe=='7':
        if pre_p[1]==p[1]-1:
            p[0]+=1
        else:
            p[1]-=1
    elif pipe=='F':
        if pre_p[1]==p[1]+1:
            p[0]+=1
        else:
            p[1]+=1
    elif mat[p[0]][p[1]]=='S':
        return l
    else:
        return 0
    l=explore_rec(mat,l+1,p,oldp)
    return l

def explore(mat,l,p,pre_p):
    
    while True:
        oldp=[p[0],p[1]]
        pipe=mat[p[0]][p[1]]
        pre_pipe=mat[pre_p[0]][pre_p[1]]
        print(p,pipe)
        if pipe=='|':
            if pre_p[0]==p[0]-1:
                p[0]+=1
            else:
                p[0]-=1
        elif pipe=='-':
            if pre_p[1]==p[1]-1:
                p[1]+=1
            else:
                p[1]-=1
        elif pipe=='L':
            if pre_p[0]==p[0]-1:
                p[1]+=1
            else:
                p[0]-=1
        elif pipe=='J':
            if pre_p[1]==p[1]-1:
                p[0]-=1
            else:
                p[1]-=1
        elif pipe=='7':
            if pre_p[1]==p[1]-1:
                p[0]+=1
            else:
                p[1]-=1
        elif pipe=='F':
            if pre_p[1]==p[1]+1:
                p[0]+=1
            else:
                p[1]+=1
        elif mat[p[0]][p[1]]=='S':
            break
        else:
            return 0
        l+=1
        pre_p=oldp
    return l
    
mat=[]
f=open('input.txt')
i=0
for l in f:
    l=l.split()[0]
    for j in range(len(l)):
        if 'S'==l[j]:
            start_pos=[i,j]
    mat.append(l)
    i+=1
    
print(start_pos)
for i in mat:
    print(i)
    
print('')
l=[]
doubleloop=[]
for [i,j] in [[1,0],[-1,0],[0,-1],[0,1]]:
    new_pos=[start_pos[0]+i,start_pos[1]+j]
    print(new_pos)
    if new_pos[0]<=len(mat)-1 and new_pos[0]>= 0 and new_pos[1] <= len(mat[0])-1 and new_pos[1] >= 0:
        out=explore(mat,1,new_pos,start_pos)
        if out in l:
            doubleloop.append(out)
        else:
            l.append(out)

print(l)
print(doubleloop)
print(doubleloop[0]/2)
