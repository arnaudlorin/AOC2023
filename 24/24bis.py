# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 22:29:28 2024

@author: artan
"""
err=1e-4

import time

class InfiniteFullSet(object):

    def __and__(self, item):
        return item

    def __rand__(self,item):
        return item

def prime(a):
    l=set()
    for i in range(2,a+1):
        if a==1:
            return l
        if a%i==0:
            while a%i==0:
                a=a//i
            l.add(i)
    return l
           
def prime2(a,lprime):
    l=set()
    for i in range(2,a+1):
        if a==1:
            return l
        if a%i==0:
            l.add(i)
            return lprime[a//i]|l
    return l

def prime4(a,lprime):
    l=set()
    if a==1:
        lprime[a]=set()
        return
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            l.add(i)
            lprime[a]=lprime[a//i]|l
            return 
    lprime[a]={a}
    
def lcm(a,b,c):
    x=prime(a)
    y=prime(b)
    if a!=0 and b!=0:
        u=x&y
        if u==set():
            return 1
    elif a==0 and b==0:
        if c==1:
            return 1
        else:
            return 0
    elif a==0:
        u=y
    elif b==0:
        u=x

    z=prime(c)
    if c!=0:
        u=u&z
    if u==set():
        return 1
    return 0

def partition(n):
    l=[]
    for i in range(n+1):
        for j in range(n-i+1):
            #if lcm(i,j,n-i-j):
            l.append([i,j,n-i-j])
    return l

def dot(x,v):
    return x[0]*v[0]+x[1]*v[1]+x[2]*v[2]

def cross_prod(a,b):
    return [a[1]*b[2]-a[2]*b[1],-a[0]*b[2]+a[2]*b[0],a[0]*b[1]-a[1]*b[0]]

def sub(a,b):
    return [a[0]-b[0],a[1]-b[1],a[2]-b[2]]
def norm(v):
    nor=(v[0]**2+v[1]**2+v[2]**2)**0.5
    v[0]/=nor
    v[1]/=nor
    v[2]/=nor

def base(v):
    if v[0]!=0 or v[1]!=0:
        v1=[-v[1],v[0],0]
    else:
        v1=[1,0,0]
    v2=cross_prod(v, v1)
    norm(v1)
    norm(v2)
    return(v1,v2)


def cross(v1,v2,p1,p2):

        det1=-v1[0]*v2[1]+v1[1]*v2[0]
        if det1!=0:
            t1=1/det1*(-v2[1]*(p2[0]-p1[0])+v2[0]*(p2[1]-p1[1]))
            if t1<0:
                return 0
            t2=1/det1*(-v1[1]*(p2[0]-p1[0])+v1[0]*(p2[1]-p1[1]))
            if t2<0:
                return 0
            x=v1[0]*t1+p1[0]
            y=v1[1]*t1+p1[1]
            if x>xmin and x<xmax and y>ymin and y<ymax:
                return (x,y)
        return 0

def cross2(v1,v2,p1,p2):

        det1=-v1[0]*v2[1]+v1[1]*v2[0]
        if det1==0:
            print('aaa')
        if det1!=0:
            t1=1/det1*(-v2[1]*(p2[0]-p1[0])+v2[0]*(p2[1]-p1[1]))
            t2=1/det1*(-v1[1]*(p2[0]-p1[0])+v1[0]*(p2[1]-p1[1]))
            if t1*t2<0:
                return 0
            x=v1[0]*t1+p1[0]
            y=v1[1]*t1+p1[1]
            return (x,y)
        return 0

def inter(dire,lv,lp):
    point=[]
    v1,v2=base(dire)
    vv1=[dot(lv[0],v1),dot(lv[0],v2)]
    x1=[dot(lp[0],v1),dot(lp[0],v2)]
    for k in range(1,len(lp)):
        vv2=[dot(lv[k],v1),dot(lv[k],v2)]
        x2=[dot(lp[k],v1),dot(lp[k],v2)]
        a=cross2(vv1, vv2, x1, x2)
        if a==0:
            return 0
        if point==[]:
            point=a
        elif abs(a[0]-point[0])>err or abs(a[1]-point[1])>err:
            return 0
    if point!=[]:
        print('aaaaaab',point)
        lz=[]
        lt=[]
        for k in range(len(lp)):
            norm(dire)
            v=[dot(lv[k],v1),dot(lv[k],v2),dot(lv[k],dire)]
            x=[dot(lp[k],v1),dot(lp[k],v2),dot(lp[k],dire)]
            t=(a[0]-x[0])/v[0]
            lt.append(t)
            lz.append(v[2]*t+x[2])
        print('z=',lz)
        speed=(lz[1]-lz[0])/(lt[1]-lt[0])
        pos=lz[0]-speed*lt[0]
        print(pos,speed)
        pos=[pos,a[0],a[1]]
        w1=[dire[0],v1[0],v2[0]]
        w2=[dire[1],v1[1],v2[1]]
        w3=[dire[2],v1[2],v2[2]]
        print(dot(pos, w1))
        print(dot(pos, w2))
        print(dot(pos, w3))
        raise Exception('find one!')
        return point
    else:
        raise Exception('shouldnt be here')        


#(partition(5000))
xmax=400000000000000
xmin=200000000000000
#xmin=7
#xmax=27
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
        
print(lp)
print(lv)

icc=0
for i in range(len(lcoord)):
    for j in range(i+1,len(lcoord)):
        if cross(lv[i],lv[j],lp[i],lp[j])!=0: 
            icc+=1
            
    
print()
print(icc)
print()
m=3

p0=lp.pop()
v0=lv.pop()
print(v0)
first_plan=cross_prod(sub(lp[0],p0), sub(lv[0],v0))
ld=0
for i in range(len(lv)):
    
    second_plan=cross_prod(sub(lp[i],p0), sub(lv[i],v0))
    if ld==0:
        prev=cross_prod(first_plan, second_plan)
        ld=prev
    else:
        ld=cross_prod(first_plan, second_plan)
        a=cross_prod(prev, ld)
        if a[0]!=0 or a[1]!=0 or a[2]!=0:
            raise Exception('problem not colinear')
V=ld
print()
i=1
v1= sub(lv[i],v0)
det = -(v1[0]*V[1]-v1[1]*V[0])
if det!=0:
    t1=1/det*(-V[1]*(p0[0]-lp[i][0])+V[0]*(p0[1]-lp[i][1]))
    t11=1/det*(-v1[1]*(p0[0]-lp[i][0])+v1[0]*(p0[1]-lp[i][1]))
    x1=[v1[j]*t1+lp[i][j] for j in range(3)]
    x11=[V[j]*t11+p0[j] for j in range(3)]
    


i=0
v1= sub(lv[i],v0)
det = -(v1[0]*V[1]-v1[1]*V[0])
if det!=0:
    t2=1/det*(-V[1]*(p0[0]-lp[i][0])+V[0]*(p0[1]-lp[i][1]))
    t21=1/det*(-v1[1]*(p0[0]-lp[i][0])+v1[0]*(p0[1]-lp[i][1]))
    x2=[v1[j]*t2+lp[i][j] for j in range(3)]
    x21=[V[j]*t21+p0[j] for j in range(3)]
    


V=[(x2[j]-x1[j])/(t2-t1) for j in range(3)]
print(V)

X=[x1[j]-V[j]*t1 for j in range(3)]
print(X[0]+X[1]+X[2])

"""

t1=time.time()
n=0
lprime={}
while n<m:
    n+=1
    print()
    print(n)
    #lprime[n]=prime2(n,lprime)
    prime4(n,lprime)
    for i in range(n+1):
        if i==0:
            ti=InfiniteFullSet()
        else:
            ti=lprime[i]
        for j in range(n-i+1):
            if j==0:
                tj=InfiniteFullSet()
            else:
                tj=lprime[j]
            if n-i-j==0:
                tk=InfiniteFullSet()
            else:
                tk=lprime[n-i-j]
            inters=ti&tj&tk
            if inters==set():
                #print(i,j,n-i-abs(j))
                a=inter([i,j,n-i-j], lv, lp)
                if a!=0:print(a)
            
                if j!=0:
                    #print(i,j,-(n-i-abs(j)))
                    a=inter([i,-j,n-i-j], lv, lp)
                    
                    if n-i-j!=0:
                        #print(i,j,-(n-i-abs(j)))
                        a=inter([i,-j,-(n-i-j)], lv, lp)
                if n-i-j!=0:
                    #print(i,j,-(n-i-abs(j)))
                    a=inter([i,j,-(n-i-j)], lv, lp)


"""

"""
t2=time.time()  
n=0
lprime={}          
while n<m:
    n+=1
    print()
    print(n)
    for i in range(n+1):
        for j in range(-(n-i),n-i+1):
            #print(i,j,n-i-abs(j))
            a=inter([i,j,n-i-abs(j)], lv, lp)
            if a!=0:print(a)
            if i==0: continue
        
            if n-i-abs(j)!=0:
                #print(i,j,-(n-i-abs(j)))
                a=inter([i,j,-(n-i-abs(j))], lv, lp)
                if a!=0:
                    raise Exception('find one!')                    
t3=time.time()  
print(t2-t1,t3-t2)    
"""   