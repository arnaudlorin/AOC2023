# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 17:20:36 2024

@author: artan
"""

def fall(i,top,bottom):
    if top[i]==set():
        return 1
    icc=1
    for j in top[i]:
        bottom[j].remove(i)
        if bottom[j]==set():
            icc+=fall(j,top,bottom)
        
    return icc
    
    
n=10
h=500

i=0
top=[]
bottom=[]
li=[]
mat=[[[0 for _ in range(h)] for _ in range(n)] for _ in range(n)]
with open('input.txt') as f:
    for l in f:
        top.append(set())
        bottom.append(set())
        i+=1
        l=l.split('~')
        s=list(map(lambda x:int(x),l[0].split(',')))
        e=list(map(lambda x:int(x),l[1].split(',')))
        if s[2]>e[2]:
            a=s.copy()
            s=e
            e=a
        find=False
        for i in range(len(li)):
            if li[i][0][2]>s[2]:
                find=True
                break
        if not find: i+=1
        li.insert(i,[s,e])
    print(li)
    for i in range(len(li)):
        
        s=li[i][0]
        e=li[i][1]
        dx=[e[i]-s[i] for i in range(3)]
        dm=max(dx)+1
        if dm==1:
            d=[0,0,0]
        else:
            d=[i//(dm-1) for i in dx]
        #print(dx,dm,d)
        heigh=0
        for k in range(s[2]+1):
            for j in range(dm):
                if mat[s[0]+j*d[0]][s[1]+j*d[1]][s[2]-k]!=0:
                    top[mat[s[0]+j*d[0]][s[1]+j*d[1]][s[2]-k]-1].add(i)
                    bottom[i].add(mat[s[0]+j*d[0]][s[1]+j*d[1]][s[2]-k]-1)
                    heigh=s[2]-k+1
            if heigh!=0:
                break
        for j in range(dm):
            mat[s[0]+j*d[0]][s[1]+j*d[1]][heigh+j*d[2]]=i+1
            
for k in range(10):
    for i in range(len(mat)):
        for j in range(len(mat)):
            print('{:5d}'.format(mat[i][j][k]),end='')
        print()
    print()
        
icc=0
for ii,i in enumerate(top):
    if i==set():
        continue
    else:
        remove=True
        bottom1=[k.copy() for k in bottom]
        a=fall(ii,top,bottom1)-1
        #print(a)
        icc+=a
            
print()
print(icc)
#85409 too high
#71404 too high