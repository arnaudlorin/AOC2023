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
    node_in_loop=[]
    while True:
        oldp=[p[0],p[1]]
        pipe=mat[p[0]][p[1]]
        node_in_loop.append([p[0],p[1]])
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
            return 0,[]
        l+=1
        pre_p=oldp
    return l,node_in_loop
    
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
pos_loop=[]
for [i,j] in [[1,0],[-1,0],[0,-1],[0,1]]:
    new_pos=[start_pos[0]+i,start_pos[1]+j]
    if new_pos[0]<=len(mat)-1 and new_pos[0]>= 0 and new_pos[1] <= len(mat[0])-1 and new_pos[1] >= 0:
        out=explore(mat,1,new_pos,start_pos)
        if out[0] in l:
            doubleloop.append(out[0])
            pos_loop.append(out[1])
        l.append(out[0])

for i in range(len(doubleloop)):
    if doubleloop[i]!=0:
        break
pos_loop=pos_loop[i]

maxi=doubleloop[i]
print(maxi)
direction_S=[]
for i in range(len(l)):
    if l[i]==maxi:
        direction_S.append(i)
if direction_S[1]<direction_S[0]:
    a=direction_S[0];direction_S[0]=direction_S[1];direction_S[1]=a
if direction_S[0]==0:
    if direction_S[1]==1:
        a='|'
    elif direction_S[1]==2:
        a='7'
    else:
        a='F'
elif direction_S[0]==1:
    if direction_S[1]==2:
        a='J'
    elif direction_S[1]==3:
        a='L'
else:
    a='-'
print(l,a)
mat_int=[['0' for _ in range(len(mat[0]))] for _ in range(len(mat))]

for [i,j] in pos_loop:
    mat_int[i][j]=mat[i][j]
    
mat_int[start_pos[0]][start_pos[1]]=a
for i in mat_int:
    print(i)      
      
ninside=0
for i in range(len(mat_int)):
    ncross=0
    for j in range(len(mat_int[0])):
        if mat_int[i][j]=='|':
            #print(i,j,ncross)
            ncross=(ncross+1) % 2
        elif mat_int[i][j]=='F' or  mat_int[i][j]=='L':
            in_=mat_int[i][j]
        elif mat_int[i][j]=='7':
            if in_=='L':
                ncross=(ncross+1) % 2
        elif mat_int[i][j]=='J':
            if in_=='F':
                ncross=(ncross+1) % 2
        elif mat_int[i][j]=='0' and ncross==1:
            ninside+=1
            print(i,j)

print(ninside)

"""
min_i=0
max_i=len(mat)
mat_int=[[-1 for _ in range(len(mat[0]))] for _ in range(len(mat))]

for [i,j] in pos_loop:
    mat_int[i][j]=0
    
nquat=1
node_quat=[]
for i in range(len(mat_int)):
    for j in range(len(mat_int[0])):
        if mat_int[i][j]==0:
            continue
        elif j>0 and mat_int[i][j-1]>0:
            mat_int[i][j]=mat_int[i][j-1]
            node_quat[mat_int[i][j]-1].append([i,j])
        else:
            if i>0 and mat_int[i-1][j]>0:
                mat_int[i][j]=mat_int[i-1][j]
                node_quat[mat_int[i][j]-1].append([i,j])
            else:
                mat_int[i][j]=nquat
                nquat+=1
                node_quat.append([[i,j]])
                
for i in mat_int:
    print(i)
    
for i in node_quat:
    print(i)

print()
ninside=0
for i in range(nquat-1):
    out=False
    print(i+1,node_quat[i])
    for [j0,k0] in node_quat[i]:
        print(j0,k0)
        for [a,b] in [[0,-1],[0,1],[-1,0],[1,0]]:
            ncross=0
            j=j0;k=k0
            while True:
                j+=a;k+=b
                print(' ',j,k,a,b,ncross)
                if j<0 or j>len(mat_int)-1 or k<0 or k>len(mat_int[0])-1:
                    if ncross==0:
                        print('a')
                        out=True
                    break
                elif mat_int[j][k]==0:
                    ncross=(ncross+1)%2
                elif  mat_int[j][k]==i+1:
                    break
            if out:
                break
        if out:
            break
    print(out)
    if not out:
        ninside+=len(node_quat[i])
        
print()
print(ninside)
"""