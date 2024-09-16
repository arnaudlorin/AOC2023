# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 08:15:04 2023

@author: artan
"""

def prime(a):
    l=[]
    for i in range(2,a+1):
        if a==1:
            return l
        if a%i==0:
            icc=0
            while a%i==0:
                a=a//i
                icc+=1
            l.append([i,icc])
    return l
            
def lcm(l):
    decompo_prime=[]
    for i in range(len(l)):
        decompo_prime.append(prime(l[i]))
    print(decompo_prime)
    intersect=decompo_prime[0]
    for i in decompo_prime[1:]:
        for j in range(len(i)):
            present=False
            for k in range(len(intersect)):
                if i[j][0]==intersect[k][0]:
                    intersect[k][1]=max(intersect[k][1],i[j][1])
                    present=True
                    break
            if not present:
                intersect.append(i[j])
    icc=1
    for i in intersect:
        icc*=i[0]**i[1]
    return intersect,icc


# Low Truth
# Hight False
class flip_flop:
    def __init__(self,direction):
        self.state=False
        self.out=direction
        self.incoming=[]
        self.order={}

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
    
    def get_state(self):
        return (self.state,)
    
class conjunction:
    def __init__(self,out):
        self.order={}
        self.incoming=[]
        self.out=out
        
    def update(self,pulse,i):
        k=self.order[i]
        self.incoming[k]=pulse
        r=False
        for j in self.incoming:
            r|=j
            if r:
                return False
        return True
    
    def get_state(self):
        j=()
        for i in self.incoming:
            j+=(i,)
        return j

def subgraph(modules,subg,i,end):
    l=[]
    for j in modules[i].out:
        if j==end:
            l.append(i)
            continue
        if j not in subg:
            subg.add(j)
            l+=subgraph(modules, subg, j, end)
    return l

def evol(broad,modules,output,n_pulses,end):
    n_pulses[1]+=1
    queue=[]
    out=[]
    for i in broad:
        queue.append([i,True,'broadcaster'])
    while queue!=[]:
        #print(queue)
        task=queue.pop(0)
        n_pulses[task[1]]+=1
        if task[0] in output:
            continue
        pulse_out=modules[task[0]].update(task[1],task[2])
        if task[0]==end:
            #print('end',end,pulse_out)
            out.append([pulse_out,n_pulses[0]+n_pulses[1]])
        if pulse_out==None:
            continue
        for i in modules[task[0]].out:
            queue.append([i,pulse_out,task[0]])
    return out

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
    k=0
    for j in direc[i]:
        modules[i].order[j]=k
        modules[i].incoming.append(True)
        k+=1

        
print() 
end='hj'
lcycle=[]
for i in broad:
    print()
    start=[i]
    subg=set()
    tip=subgraph(modules,subg,i,end)
    tip=tip[0]
    print(subg)
    subg=list(subg)
    lpulse=[]
    ini=modules[i].out
    lstate=set()
    truth_table=[]
    ii=0
    while True:
        ii+=1
    #for k in range(1000):
        npulses=[0,0]
        pulse=evol(start, modules, output, npulses,tip)
        #print(pulse)
        tstat=()
        for j in subg:
            tstat+=modules[j].get_state()
        if tstat in lstate:
            break
        else:
            lstate.add(tstat)
            for j in pulse:
                if not j[0]:
                    lii=ii
                    lcycle.append(lii)
            truth_table.append(pulse)
        #if npulses in lpulse:
        #    break
        #else:
    print(ii)
    for i in truth_table:
        for j in i:
            if j[0]==False:
                print(i)
    print(lcycle)
    print(lcm(lcycle))
    #print(truth_table)
    #print(lpulse)