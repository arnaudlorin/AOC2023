# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 10:28:17 2023

@author: artan
"""

# deep first, don't work
def explore_d(i,j,n,step,step_max,mat):
    if step==step_max+1:
        return n
    mat[i][j]=step
    if step%2==0:
        n+=1
    if i>0 and mat[i-1][j]==0:
        n=explore(i-1,j,n,step+1,step_max,mat)
    if i<len(mat)-1 and mat[i+1][j]==0:
        n=explore(i+1,j,n,step+1,step_max,mat)
    if j>0 and mat[i][j-1]==0:
        n=explore(i,j-1,n,step+1,step_max,mat)
    if j<len(mat)-1 and mat[i][j+1]==0:
        n=explore(i,j+1,n,step+1,step_max,mat)
        
    return n

#  Breath first search
def explore(i,j,n,step,step_max,mat,queue):
    while True:
        if step==step_max+1:
            break
        if step%2==0:
            n+=1
        step+=1
        if i>0 and mat[i-1][j]==0:
            mat[i-1][j]=step
            queue.append([i-1,j,step])
        if i<len(mat)-1 and mat[i+1][j]==0:
            mat[i+1][j]=step
            queue.append([i+1,j,step])
        if j>0 and mat[i][j-1]==0:
            mat[i][j-1]=step
            queue.append([i,j-1,step])
        if j<len(mat)-1 and mat[i][j+1]==0:
            mat[i][j+1]=step
            queue.append([i,j+1,step])
        
        if queue!=[]:
            todo=queue.pop(0)
            i=todo[0]
            j=todo[1]
            step=todo[2]  
        else:
            break
    return n

mat=[]
i=0
with open('input.txt') as f:
    for l in f:
        l=l.split()[0]
        ll=[]
        for j in range(len(l)):
            if l[j]=='#':
                ll.append(-1)
            else:
                ll.append(0)
                if l[j]=='S':
                    istart=j
                    jstart=i
        i+=1
        mat.append(ll)
for i in mat:
    print(i)
max_step=64
result=explore(istart, jstart, 0, 0, max_step, mat,[])
print(result-1)
print(len(mat))
"""
for i in mat:
    for j in i:
        print('{:3d}'.format(j),end='')
    print('')
"""