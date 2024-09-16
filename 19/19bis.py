# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 08:23:46 2023

@author: artan
"""


def progress(workflow,objet):
    for condition in workflow[:-1]:
        #print(condition[1]*(objet[condition[0]]-condition[2]))
        if condition[1]*(objet[condition[0]]-condition[2])>0:
            return condition[3]
    return workflow[-1]

def cut_objet(ob,limit,index,s):
    obj=[]
    for i in ob:
        obj.append(i.copy())
    obj[index][(1-s)//2]=limit+s
    ob[index][(s+1)//2]=limit
    return obj

def progress_m(workflow,objet):
    objet_list=[]
    for condition in workflow[:-1]:
        if condition[1]*(objet[condition[0]][0]-condition[2])>0 and condition[1]*(objet[condition[0]][1]-condition[2])>0:
            objet_list.append([objet,condition[3]])
            return objet_list
        elif condition[1]*(objet[condition[0]][0]-condition[2])<0 and condition[1]*(objet[condition[0]][1]-condition[2])<0:
            continue
        else:
            #print(objet,condition[2],condition[0],condition[1])
            obj=cut_objet(objet,condition[2],condition[0],condition[1])
            objet_list.append([obj,condition[3]])
    objet_list.append([objet,workflow[-1]])
    return objet_list
    

def count(obj):
    n=1
    for i in obj:
        n*=(i[1]-i[0]+1)
    return n
        
workflows={}
with open('input.txt') as f:
    for l in f:
        if l=='\n':
            break
        l=l.split()[0]
        name=l.split('{')[0]
        conditions=l.split('{')[1][:-1].split(',')
        condition_list=[]
        for i in conditions[:-1]:
            part=i[0]
            if part=='x':
                part=0
            elif part=='m':
                part=1
            elif part=='a':
                part=2
            else:
                part=3
            order=i[1]
            if i[1]=='<':
                order=-1
            else:
                order=1
            number=int(i[2:].split(':')[0])
            out=i.split(':')[1]
            condition_list.append([part,order,number,out])
        condition_list.append(conditions[-1])
        workflows[name]=condition_list
        
    print(workflows)
    print()
    
maxn=4000
objet=[[1,maxn] for _ in range(4)]
name='in'
todo=[[objet,name]]
nposs=0  
i=0
while True:
    i+=1
    toprocess=todo.pop()
    name=progress_m(workflows[toprocess[1]],toprocess[0])
    #print(name)
    for j in name:
        if j[1]=='A':
            nposs+=count(j[0])
        elif j[1]!='R':
            todo.append(j)
    #print(todo)
    if todo==[]:
        break
            
print(nposs)    
"""
print(accepted)
result=0
for i in accepted:
    for j in i:
        result+=j
print(result)
"""