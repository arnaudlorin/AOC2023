# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 12:17:00 2024

@author: artan
"""

def walk(p,lasp,icc,visited):
    
    
    result=[]
    end=True
    while end:
        icc+=1
        if p in visited:
            return result
        if p==(len(carte)-1,len(carte)-2):
            print('exit',visited,icc)
            return [icc]
        visited.add(p)
        direction={(0,1),(0,-1),(1,0),(-1,0)}
        direction.remove(lasp)
        out=[]
        for d in direction:
            if carte[p[0]+d[0]][p[1]+d[1]]=='.':
                out.append(d)
        d=out.pop()
        for i in out:
            visited1=visited.copy()
            wa=walk((p[0]+i[0],p[1]+i[1]),(-i[0],-i[1]),icc,visited1)
            if wa!=0:
                result+=wa
        p=(p[0]+d[0],p[1]+d[1])
        lasp=(-d[0],-d[1])
    print('return',result)
    return result

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
        li=[]
        for i in l.split()[0]:
            if i=='#': li.append('#')
            else: li.append('.')
        carte.append(li)
      
print(carte)
a=0
start=(0,1)
d=(-1,0)

            
            
result=walk(start,d,-1,set())
print(result)
print(max(result))
"""
def walk(p,lasp,icc,visited):
    
    
    result=[]
    end=True
    while end:
        icc+=1
        if p in visited:
            return result
        if p==(len(carte)-1,len(carte)-2):
            print('exit',visited,icc)
            return [icc]
        visited.add(p)
        direction={(0,1),(0,-1),(1,0),(-1,0)}
        direction.remove(lasp)
        out=[]
        for d in direction:
            if carte[p[0]+d[0]][p[1]+d[1]]=='.':
                out.append(d)
        d=out.pop()
        for i in out:
            visited1=visited.copy()
            wa=walk((p[0]+i[0],p[1]+i[1]),(-i[0],-i[1]),icc,visited1)
            if wa!=0:
                result+=wa
        p=(p[0]+d[0],p[1]+d[1])
        lasp=(-d[0],-d[1])
    print('return',result)
    return result
"""