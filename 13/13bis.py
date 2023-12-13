# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 10:50:02 2023

@author: artan
"""

import time


# Return a set, easy to do intersections of the symetries of each row
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
    return set(new_sym)

# Return the symetries that work on one line
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

def swap(l,n):
    if l[n]=='.':
        l[n]='#'
    else:
        l[n]='.'
        
def check_mat(mat):
    mat_sym=[]
    lsym=[2*i+1 for i in range(len(mat[0])-1)]
    for col in mat:
        mat_sym.append(check_sym_set(col,lsym))
    for i in range(len(mat)):
        lsym=set([2*i+1 for i in range(len(mat[0])-1)])
        for j in range(i):
            lsym=mat_sym[j]&lsym
        for j in range(i+1,len(mat)):
            lsym=mat_sym[j]&lsym
        avoid=lsym&mat_sym[i]
        lsym=lsym-avoid
        if lsym==set():
            continue
        col=[ i for i in mat[i]]
        for j in range(len(col)):
            swap(col,j)
            out=check_sym_set(col, lsym)
            if out!=set() and out!=avoid:
                return list(out)[0]
            swap(col,j)
    return 0
        
mat=[]
f=open('input.txt')
result=0

for l in f:
    if l!='\n':
        l=l.split()[0]
        print(l)
        mat.append(l)
    else:
        print()
        sym=check_mat(mat)
        print(sym)
        if sym==0:
            mat=transpose(mat)
            sym=check_mat(mat)
            print(sym)
            result+=100*(int((sym+1)/2))
        else:
            result+=int((sym+1)/2)
        mat=[]
        
print(result)