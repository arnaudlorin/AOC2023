# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 10:50:02 2023

@author: artan
"""

import time


def check_sym_set(l,lsym):
    n=len(l)
    new_sym=[]
    for isym in lsym:
        sym=True
        if isym<=n-1:
            start=0
            end=int((isym+1)/2)
        else:
            start=int((isym)/2)+1
            end=n
        for j in range(start,end):
            if l[j]!=l[isym-j]:
                sym=False
                break
        if sym:
            new_sym.append(isym)
    return new_sym

def check_sym(l,lsym):
    n=len(l)
    new_sym=[]
    for isym in lsym:
        sym=True
        if isym<=n-1:
            start=0
            end=int((isym+1)/2)
        else:
            start=int((isym)/2)+1
            end=n
        for j in range(start,end):
            if l[j]!=l[isym-j]:
                sym=False
                break
        if sym:
            new_sym.append(isym)
    return new_sym

def transpose(mat):
    mat1=[[0 for i in range(len(mat))] for j in range(len(mat[0]))]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat1[j][i]=mat[i][j]
    return mat1

def check_mat(mat):
        lsym=[2*i+1 for i in range(len(mat[0])-1)]
        for col in mat:
            lsym=check_sym(col,lsym)
            if lsym==[]:
                break
    
mat=[]
f=open('input.txt')
result=0

for l in f:
    if l!='\n':
        l=l.split()[0]
        #print(l)
        mat.append(l)
    else:
        print()
        lsym=[2*i+1 for i in range(len(mat[0])-1)]
        for col in mat:
            lsym=check_sym(col,lsym)
            if lsym==[]:
                break
        print(lsym)
        if lsym!=[]:
            for i in lsym:
                result+=int((i+1)/2)
            if lsym[0]%2==0:
                print('-----',lsym)
                #raise Exception('several sym')
        mat=transpose(mat)
        lsym=[2*i+1 for i in range(len(mat[0])-1)]
        for col in mat:
            lsym=check_sym(col,lsym)
            if lsym==[]:
                break
        print(lsym)
        if lsym!=[]:
            #for i in lsym:
            #    print(lsym,int((i+1)/2))
            #    result+=100*(int((i+1)/2))
            result+=100*(int((lsym[-1]+1)/2))
        mat=[]
        
        if len(lsym)>1:
            print(lsym)
            raise Exception('several sym')
        
print(result)