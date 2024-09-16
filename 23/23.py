# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 12:17:00 2024

@author: artan
"""

def walk(p,lasp,icc,visited):
    
    end=True
    while end:
        icc+=1
        if p==(len(carte)-1,len(carte)-2):
            print('exit',visited)
            return [icc]
        direction={(0,1),(0,-1),(1,0),(-1,0)}
        direction.remove(lasp)
        for d in direction:
            if carte[p[0]+d[0]][p[1]+d[1]]=='.':
                p=(p[0]+d[0],p[1]+d[1])
                lasp=(-d[0],-d[1])
                break
            elif carte[p[0]+d[0]][p[1]+d[1]]=='#':
                continue
            else:
                icc=crossing((p[0]+2*d[0],p[1]+2*d[1]),d,icc+1,visited)
                end=False
                break
    return icc
def crossing(p,lasp,icc,visited):
    if p in visited:
        return 0
    visited.add(tuple(p))
    out=[]
    d=[]
    if carte[p[0]-1][p[1]]=='^': out.append((1,0))
    if carte[p[0]+1][p[1]]=='v': out.append((-1,0))
    if carte[p[0]][p[1]+1]=='>': out.append((0,-1))
    if carte[p[0]][p[1]-1]=='<': out.append((0,1))
    for i in out:
            
        visited1=visited.copy()
        d+=walk((p[0]-2*i[0],p[1]-2*i[1]),i,icc+2,visited1)

    return d

carte=[]
with open('input.txt') as f:
    for l in f:
      carte.append(list(l.split()[0]))
      
print(carte)
a=0
start=(0,1)
d=(-1,0)

            
            
result=walk(start,d,-1,set())
print(result)
print(max(result))