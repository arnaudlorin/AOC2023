# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 08:58:53 2023

@author: artan
"""

def sort_t(l):
    for i in range(len(l)):
        mini=l[i][0]
        iindex=i
        for j in range(i+1,len(l)):
            if l[j][0]<mini:
                mini=l[j][0]
                iindex=j
        a=l[iindex]
        l[iindex]=l[i]
        l[i]=a
        
def sort(l):
    for i in range(len(l)):
        mini=l[i]
        iindex=i
        for j in range(i+1,len(l)):
            if l[j]<mini:
                mini=l[j]
                iindex=j
        a=l[iindex]
        l[iindex]=l[i]
        l[i]=a
        
        
def inside(mat):
    ninside=0
    for i in range(len(mat)):
        ncross=0
        for j in range(len(mat[0])):
            if mat[i][j]=='|':
                #print(i,j,ncross)
                ncross=(ncross+1) % 2
            elif mat[i][j]=='F' or  mat[i][j]=='L':
                in_=mat[i][j]
            elif mat[i][j]=='7':
                if in_=='L':
                    ncross=(ncross+1) % 2
            elif mat[i][j]=='J':
                if in_=='F':
                    ncross=(ncross+1) % 2
            elif mat[i][j]=='.' and ncross==1:
                ninside+=1
            if mat[i][j]!='.':
                ninside+=1
    
    return ninside
    
def inside_side(list_vert,mini,maxi):
    ninside=0
    nll=[]
    for i in range(mini,maxi+1):
        ncross=0
        z=0
        prev=None
        nl=0
        for j in list_vert:
            if i==j[1]:
                if ncross==0:
                    prev=ncross
                    ncross=2
                elif ncross==1:
                    ninside+=j[0]-z
                    nl+=j[0]-z
                    prev=ncross
                    ncross=2
                elif ncross==2:
                    ninside+=j[0]-z+1-prev
                    nl+=j[0]-z+1-prev
                    ncross=prev
                elif ncross==3:
                    ninside+=j[0]-z+prev
                    nl+=j[0]-z+prev
                    ncross=1-prev
                z=j[0]
            elif i==j[2]:
                if ncross==0:
                    prev=ncross
                    ncross=3
                elif ncross==1:
                    ninside+=j[0]-z
                    nl+=j[0]-z
                    prev=ncross
                    ncross=3
                elif ncross==2:
                    ninside+=j[0]-z+prev
                    nl+=j[0]-z+prev
                    ncross=(prev+1)%2
                elif ncross==3:
                    ninside+=j[0]-z+1-prev
                    nl+=j[0]-z+1-prev
                    ncross=prev
                z=j[0]
            elif i>j[1] and i<j[2]:
                if ncross==1:
                    ninside+=j[0]-z+1
                    nl+=j[0]-z+1
                    ncross=0
                else:
                    z=j[0]
                    ncross=1
        if nl!=0 and nl not in nll:
            print(nl,i)
            nll.append(nl)
    
    return ninside

def surface_one_line(list_vert,i):
    ncross=0
    z=0
    ninside=0
    for j in list_vert:
        if i>j[1] and i<j[2]:
            if ncross==1:
                ninside+=j[0]-z+1
                ncross=0
            else:
                z=j[0]
                ncross=1
    return ninside

def surface_intersection_line(list_vert,i):
    ninside=0
    ncross=0
    z=0
    prev=None
    for j in list_vert:
        if i==j[1]:
            if ncross==0:
                prev=ncross
                ncross=2
            elif ncross==1:
                ninside+=j[0]-z
                prev=ncross
                ncross=2
            elif ncross==2:
                ninside+=j[0]-z+1-prev
                ncross=prev
            elif ncross==3:
                ninside+=j[0]-z+prev
                ncross=1-prev
            z=j[0]
        elif i==j[2]:
            if ncross==0:
                prev=ncross
                ncross=3
            elif ncross==1:
                ninside+=j[0]-z
                prev=ncross
                ncross=3
            elif ncross==2:
                ninside+=j[0]-z+prev
                ncross=(prev+1)%2
            elif ncross==3:
                ninside+=j[0]-z+1-prev
                ncross=prev
            z=j[0]
        elif i>j[1] and i<j[2]:
            if ncross==1:
                ninside+=j[0]-z+1
                ncross=0
            else:
                z=j[0]
                ncross=1
    return ninside

# Avoid computing surface for every line, but only for one line between two change of direction
def inside_side2(list_vert,pos_vert,mini,maxi):
    ninside=0
    surface=0
    prev_i=pos_vert[0]
    for i in pos_vert:
        ninside+=surface_intersection_line(list_vert, i)
        ninside+=surface*(i-prev_i-1)
        surface=surface_one_line(list_vert,i+1)
        #print(surface_one_line(list_vert,i+1),i+1)
        prev_i=i
    
    return ninside
    
list_pos=[[0,0]]
list_vert=[]
pos=[0,0]
maxi=0
mini=0
with open('input.txt') as f:
    for l in f:
        l=l.split()[2][2:-1]
        lenght=int(l[:5],16)
        if l[-1]=='0': #right
            pos[1]+=lenght
        elif l[-1]=='1': #down
            pos[0]+=lenght
            list_vert.append([pos[1],list_pos[-1][0],pos[0]])
            if pos[0]>maxi:
                maxi=pos[0]
        elif l[-1]=='2': #left
            pos[1]+=-lenght
        elif l[-1]=='3': # up
            pos[0]+=-lenght
            list_vert.append([pos[1],pos[0],list_pos[-1][0]])
            if pos[0]<mini:
                mini=pos[0]
        
        list_pos.append([pos[0],pos[1]])
        
#print(list_vert)
sort_t(list_vert)

pos_vert=[]
for i in list_vert:
    if i[1] not in pos_vert:
        pos_vert.append(i[1])
    if i[2] not in pos_vert:
        pos_vert.append(i[2])
print(mini)
print(maxi)
sort(pos_vert)
print()
#print(inside_side(list_vert,mini,maxi))
print()
print(inside_side2(list_vert,pos_vert,mini,maxi))
#print(list_pos)
