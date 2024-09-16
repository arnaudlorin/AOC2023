# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 08:15:04 2023

@author: artan
"""

class flip_flop:
    def __init__(self,direction):
        self.state=False
        self.out=direction
        self.incoming={}

    def update(self,pulse,i):
        #print(self.state)
        if pulse:
            if self.state:
                self.state=False
                return True
            else:
                self.state=True
                return False
        return None
    
class conjunction:
    def __init__(self,out):
        self.incoming={}
        self.out=out
        
    def update(self,pulse,i):
        self.incoming[i]=pulse
        r=False
        for j in self.incoming.values():
            r|=j
            if r:
                return False
        return True
    
def evol(broad,modules,output,n_pulses):
    n_pulses[1]+=1
    queue=[]
    for i in broad:
        queue.append([i,True,'broadcaster'])
    while queue!=[]:
        #print(queue)
        task=queue.pop(0)
        n_pulses[task[1]]+=1
        if task[0] in output:
            continue
        pulse_out=modules[task[0]].update(task[1],task[2])
        if pulse_out==None:
            continue
        for i in modules[task[0]].out:
            queue.append([i,pulse_out,task[0]])
    #return n_pulses
modules={}
direc={}
with open('input.txt') as f:
    for l in f:
        l=l.split('\n')[0]
        l=l.split('-> ')
        direction=l[1].split(', ')
        name=l[0][:-1]
        if 'broadcaster' in name:
            broad=direction
        else:
            name=name[1:]
        for name1 in direction:
            if name1 in direc:
                direc[name1].append(name)
            else:
                direc[name1]=[name]

        if l[0][0]=='%':
            modules[name]=flip_flop(direction)
        else:
            modules[name]=conjunction(direction)
         
output=set()
for i in direc:
    if i not in modules:
        output.add(i)
        continue
    for j in direc[i]:
        modules[i].incoming[j]=True
        
npulses=[0,0]
print()
n=1000
for _ in range(n):
    evol(broad,modules,output,npulses)
print(npulses)
print(npulses[0]*npulses[1])