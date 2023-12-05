# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 09:09:11 2023

@author: artan
"""

number=['0','1','2','3','4','5','6','7','8','9']

def test_line_b(line,j):
    for k in range(j,-1,-1):
        if line[k] not in number:
            k+=1
            break
    return int(line[k:j+1])
        
def test_line_f(line,j):
    for k in range(j,len(line)):
        if line[k] not in number:
            k-=1
            break
    return int(line[j:k+1])

def test_line_d(line,j):
    for k in range(j,len(line)):
        if line[k] not in number:
            k-=1
            break
    for l in range(j,-1,-1):
        if line[l] not in number:
            l+=1
            break
    return int(line[l:k+1])

def test_off(line,j):
    ln=0
    if line[j] == '.':
        if line[j-1] in number:
            ln+=test_line_b(line, j-1)
        if line[j+1] in number:
            ln+=test_line_f(line, j+1)
    else:
        ln+=test_line_d(line, j)
    return ln
        
def test(mat,i,j):
    ln=0
    if mat[i][j-1] in number:
        ln+=test_line_b(mat[i], j-1)
    if mat[i][j+1] in number:
        ln+=test_line_f(mat[i], j+1)
    ln+=test_off(mat[i-1], j)
    ln+=test_off(mat[i+1], j)
    return ln
            
        
mat=[]
f=open('input.txt')
for l in f:
    l=l.split('\n')[0]
    mat.append(l)

count=0
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j] not in number and mat[i][j] != '.':
            count+=test(mat,i,j)
print(count)