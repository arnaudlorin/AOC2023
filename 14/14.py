# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 07:31:11 2023

@author: artan
"""

# Compute the load on the North beam, ASSUMING a tilt toward the north
def result(npos,fix_pos):
    nrow=len(npos)
    result=0
    for i in range(nrow):
        for j in range(len(npos[i])):
            if npos[i][j]!=0:
                result+=sum_int_m(nrow-fix_pos[i][j]-1,npos[i][j]-1)
    return result

# Compute the load on the North beam, ASSUMING a tilt toward the east
def result_e(npos,fix_pos):
    nrow=len(npos)
    result=0
    for i in range(nrow):
        for j in range(len(npos[i])):
            if npos[i][j]!=0:
                result+=(nrow-i)*npos[i][j]
    return result

# Check if 2 lists of position are egals.
def egal(npos,old_npos):
    for i in range(len(npos)):
        if npos[i]!=old_npos[i]:
            return False
        
    return True

# Do 4 tilt: north,west,south,east
def cycle(npos,fix_pos):
    npos=tilt(npos, fix_pos[3])
    npos=tilt(npos, fix_pos[0])
    npos=tilt(npos, fix_pos[1])
    npos=tilt(npos, fix_pos[2])
    return npos

# Do a tilt, the pos list is changed
def tilt(pos,fix_pos):
    new_pos=[[0] for i in range(len(pos))]
    for i in range(len(pos)):
        for k in range(pos[i][0]):
            new_pos[nrow-k-1][-1]+=1
        for j in range(1,len(pos[i])):
            new_pos[nrow-fix_pos[i][j]-1].append(0)
            for k in range(pos[i][j]):
                new_pos[nrow-fix_pos[i][j]-k-2][-1]+=1
    return new_pos
    
# Sum of i for i in [s,n]
def sum_int(s,n):
    return int((n-s+1)*(n+s)/2)
    
#sum from s with p element
def sum_int_l(s,p):
    return int((p+1)*(2*s+p)/2)

#sum from n with p elements decroissant
def sum_int_m(n,p):
    return int((p+1)*(2*n-p)/2)


inputt='input.txt'
with open(inputt) as f:
    n=len(f.readline().split()[0])
npos=[[0] for i in range(n)]
fix_pos_n=[[-1] for _ in range(n)]
fix_pos_w=[[] for _ in range(n)]
fix_pos_s=[[-1] for _ in range(n)]
fix_pos_e=[[-1] for _ in range(n)]
i=0
f=open(inputt)
for l in f:

    for j in range(n):
        if l[j]=='#':
            fix_pos_n[j].append(i)
            fix_pos_w[i].append(j)
            npos[j].append(0)
        elif l[j]=='O':
            npos[j][-1]+=1
    i+=1
       
nrow=i

# Prepare the list of fixed rock seen for a west orientation, xaxis=row,yaxis=column, both reversed
fix_pos_w_1=[[-1] for _ in range(n)]
for i in range(len(fix_pos_w)):
    for j in range(len(fix_pos_w[i])):
        fix_pos_w_1[n-i-1].append(fix_pos_w[i][j])
fix_pos_w=fix_pos_w_1

# Prepare list of fixed rock from south
for i in range(len(fix_pos_n)):
    for j in range(len(fix_pos_n[i])-1,0,-1):
        fix_pos_s[n-1-i].append(nrow-fix_pos_n[i][j]-1)
     
# Prepare list of fixed rock from east
for i in range(len(fix_pos_w)):
    for j in range(len(fix_pos_w[i])-1,0,-1):
        fix_pos_e[n-1-i].append(nrow-fix_pos_w[i][j]-1)
       


print('Ini')
print(npos)
print('Answer to the first part is:')
npos1=npos.copy()
print(result(npos,fix_pos_n))

# Do a first incomplete cycle as we start from north.
print()
fix_pos=[fix_pos_n,fix_pos_w,fix_pos_s,fix_pos_e]
npos=tilt(npos, fix_pos_n)
npos=tilt(npos, fix_pos_w)
npos=tilt(npos, fix_pos_s)


print('First cycle')

# Realize ncvg cycle to try to reach a converged cycle
ncvg=10**3-1
for i in range(ncvg):
    npos=cycle(npos,fix_pos)
    
print('After',ncvg+1,'cycle')

# Try to find a periodicity
ncycle=10**9-ncvg
old_npos=npos.copy()
for i in range(ncycle):
    npos=cycle(npos,fix_pos)
    if egal(npos,old_npos):
        break

period=i+1
print('Loop find with periodicity',period,'period,we are at', ncvg+1+period,'cycle')
#print(npos)
print()

# Compute the state that correspond to the ncycle state modulo the periodicity
for j in range(1,(ncycle)%period):
    npos=cycle(npos,fix_pos)

#Compute the result
print(result_e(npos,fix_pos_e))
print()

    




