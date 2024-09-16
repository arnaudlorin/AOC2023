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
def explore(i,j,step_max,mat):
    step_max+=1
    parity=step_max%2
    odd=0
    even=0
    step=1
    queue=[]
    mat[i][j]=step
    while True:
        if step==step_max+1:
            break
        if step%2==0: # Step start at 1 so 2 represent actually 1 step (odd)
            odd+=1
        else:
            even+=1
        if step<step_max:
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
    return even,odd

mat=[]
i=0
nplot=0
with open('input.txt') as f:
    for l in f:
        l=l.split()[0]
        ll=[]
        for j in range(len(l)):
            if l[j]=='#':
                ll.append(-1)
            else:
                ll.append(0)
                nplot+=1
                if l[j]=='S':
                    istart=j
                    jstart=i
        i+=1
        mat.append(ll)

max_step=26501365
n=len(mat)
print(n,nplot)
print(istart,jstart)


mat1=[i.copy() for i in mat]
evenodd=explore(istart, jstart, max_step, mat1)
print("Plot reacheable with even/odd",evenodd)



nwidth=((max_step-65)/n)
parity=int((max_step)%2)
print(max_step,nwidth,parity)

n1=(2*((nwidth)//2))**2 # Number of even bloc
n2=(2*((nwidth+1)//2)-1)**2# Number of odd bloc
print(n1,n2)

nwalk=n1*evenodd[1-parity]+n2*evenodd[parity]
print(nwalk)
#nwalk+=evenodd[parity] # Central spot

m=n
ii=[]
for i in range(n):
    for j in range(m):
        if mat1[i][j]==0:
            ii.append([i,j])
       # print('{:4d}'.format(mat1[i][j]),end='')
    #print('')
#print(ii)

max_step=130
parityn=(n-1)%2
mat1=[i.copy() for i in mat]
result_e=explore(istart, 0, max_step, mat1)

mat1=[i.copy() for i in mat]
result_w=explore(istart, n-1, max_step, mat1)

mat1=[i.copy() for i in mat]
result_s=explore(0, jstart, max_step, mat1)

mat1=[i.copy() for i in mat]
result_n=explore(n-1, jstart, max_step, mat1)

nwalk+=result_e[parityn]+result_w[parityn]+result_n[parityn]+result_s[parityn]


# Small triangle
max_step=64
mat1=[i.copy() for i in mat]
result_se1=explore(0,0, max_step, mat1)
mat1=[i.copy() for i in mat]
result_sw1=explore(0,n-1, max_step, mat1)
mat1=[i.copy() for i in mat]
result_ne1=explore(n-1,0, max_step, mat1)
mat1=[i.copy() for i in mat]
result_nw1=explore(n-1,n-1, max_step, mat1)
nwalk+= (nwidth)*(result_se1[0]+result_sw1[0]+result_ne1[0]+result_nw1[0])

# Big triangl
max_step=195
mat1=[i.copy() for i in mat]
result_se2=explore(0,0, max_step, mat1)
mat1=[i.copy() for i in mat]
result_sw2=explore(0,n-1, max_step, mat1)
mat1=[i.copy() for i in mat]
result_ne2=explore(n-1,0, max_step, mat1)
mat1=[i.copy() for i in mat]
result_nw2=explore(n-1,n-1, max_step, mat1)
nwalk+= (nwidth-1)*(result_se2[1]+result_sw2[1]+result_ne2[1]+result_nw2[1])

print()
print(int(nwalk),610158187362102,int(610158187362102-nwalk))
# good answer 610158187362102
# too low 610158132928691 610158132936142 610158187354400 610158187361922
