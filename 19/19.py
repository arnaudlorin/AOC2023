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
    object_list=[]
    for l in f:
        l=l.split()[0]
        objet=l[1:-1].split(',')
        o=[0]*4
        for i in range(len(objet)):
            o[i]=int(objet[i].split('=')[1])
        object_list.append(o)
print(object_list)
         
accepted=[]   
for i in object_list:
    name='in'
    while True:
        name=progress(workflows[name],i)
        if name=='A':
            accepted.append(i)
            break
        elif name=='R':
            break
        
print(accepted)
result=0
for i in accepted:
    for j in i:
        result+=j
print(result)