# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 22:29:28 2024

@author: artan
"""

xmax=400000000000000
xmin=200000000000000
ymin=xmin
ymax=xmax
lcoord=[]
lp=[]
lv=[]
with open('input.txt') as f:
    for l in f:
        [p,v]=l.split('@')
        p=list(map(lambda x:int(x),p.split(',')))
        v=list(map(lambda x:int(x),v.split(',')))
        idet=1/(p[0]*v[1]-p[1]*v[0])
        
        lcoord.append([idet*v[1],-idet*v[0]])
        lp.append(p)
        lv.append(v)
        
icc=0
for i in range(len(lcoord)):
    for j in range(i+1,len(lcoord)):
        det=lcoord[i][0]*lcoord[j][1]-lcoord[i][1]*lcoord[j][0]
        #]print(det)
        if det!=0:
            x=1/det*(lcoord[j][1]-lcoord[i][1])
            y=1/det*(lcoord[i][0]-lcoord[j][0])
            if x>xmin and x<xmax and y>ymin and y<ymax:
                doti=(x-lp[i][0])*lv[i][0]+(y-lp[i][1])*lv[i][1]
                if doti<0:continue
                dotj=(x-lp[j][0])*lv[j][0]+(y-lp[j][1])*lv[j][1]
                if dotj<0:continue
                icc+=1

print(icc)