# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 08:13:02 2023

@author: artan
"""


def hash1(s):
    result=0
    for c in s:
        result=(17*(result + ord(c))) % 256
    return result

hashmap=[[] for _ in range(256)]
result=0
with open('input.txt') as f:
    for l in f:
        l=l.split(',')
        for i in l:
            for j in range(len(i)):
                if i[j]=='-':
                    op=0
                    break
                elif i[j]=='=':
                    op=1
                    break
            label=i[:j]
            h=hash1(label)
            if op:
                if hashmap[h]==[]:
                    hashmap[h].append([label,i[-1]])
                else:
                    find=False
                    for j in hashmap[h]:
                        if j[0]==label:
                            j[1]=i[-1]
                            find=True
                            break
                    if not find:
                        hashmap[h].append([label,i[-1]])
                
            else:
                for j in range(len(hashmap[h])):
                    if hashmap[h][j][0]==label:
                        hashmap[h].pop(j)
                        break
                
result=0
print(hashmap[0:4])    
for i in range(len(hashmap)):
    for j in range(len(hashmap[i])):
        result+=(i+1)*(j+1)*int(hashmap[i][j][1])
print(result)