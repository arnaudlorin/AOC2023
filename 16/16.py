# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 07:16:07 2023

@author: artan
"""


def mirr90(d):
    a=-d[0]
    d[0]=-d[1]
    d[1]=a
    return d
def mirr(d):
    a=d[0]
    d[0]=d[1]
    d[1]=a
    return d

def explore(mat,check,pos,d,n,ind):
    dist=0
    if d[0]==0:
        if d[1]==1:
            end=n-pos[1]-1
        else:
            end=pos[1]
    elif d[0]==1:
        end=n-pos[0]-1
    else:
        end=pos[0]
    for i in range(end):
        pos[0]+=d[0]
        pos[1]+=d[1]
        if check[pos[0]][pos[1]]==[]:
            dist+=1
        if d in check[pos[0]][pos[1]]:
            break
        else:
            check[pos[0]][pos[1]].append([d[0],d[1]])
        if mat[pos[0]][pos[1]]=='\\':
            d=mirr(d)
            dist+=explore(mat, check, pos, d, n,ind+'  ')
            break
        elif mat[pos[0]][pos[1]]=='/':
            d=mirr90(d)
            dist+=explore(mat, check, pos, d, n,ind+'  ')
            break
        elif mat[pos[0]][pos[1]]=='|':
            if d[1]!=0:
                dist+=explore(mat,check,[pos[0],pos[1]],[1,0],n,ind+'  ')
                dist+=explore(mat,check,[pos[0],pos[1]],[-1,0],n,ind+'  ')
                break
        elif mat[pos[0]][pos[1]]=='-':
            if d[0]!=0:
                dist+=explore(mat,check,[pos[0],pos[1]],[0,1],n,ind+'  ')
                dist+=explore(mat,check,[pos[0],pos[1]],[0,-1],n,ind+'  ')
                break
    return dist
mat=[]
with open('input.txt') as f:
    for l in f:
        l=l.split()[0]
        mat.append(l)
print(mat)
n=len(mat)
result=0
for i in range(n):
    check= [[[] for _ in range(n)] for _ in range(n)]
    result=max(result,explore(mat,check,[-1,i],[1,0],n,''))
    check= [[[] for _ in range(n)] for _ in range(n)]
    result=max(result,explore(mat,check,[n,i],[-1,0],n,''))
print(result)
print('Vertical check')
for i in range(n):
    check= [[[] for _ in range(n)] for _ in range(n)]
    result=max(result,explore(mat,check,[i,-1],[0,1],n,''))
    check= [[[] for _ in range(n)] for _ in range(n)]
    result=max(result,explore(mat,check,[i,n],[0,-1],n,''))


    
print(result)