# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 11:27:23 2023

@author: artan
"""


class ens:
    def __init__(self,s,e):
        self.start=s
        self.end=e
        
    def print(self):
        print('[{},{}]'.format(self.start,self.end))
        
class maps: 
    def __init__(self,s,e,o):
        self.start=s
        self.end=e
        self.offset=o
        
    def print(self):
        print('[{},{}] {}'.format(self.start,self.end,self.offset))

    def propagate(self,ra):
        #print(self.start,self.end,ra.start,ra.end)
        if self.start>=ra.start:
            if self.start>ra.end: # disjoint
                return ens(0,-1),
            elif self.end<=ra.end: # self included in ra
                newra=ens(self.start+self.offset,self.end+self.offset)
                oldra=ens(self.end+1,ra.end)
                ra.end=self.start-1
                return newra,oldra
            else: # self to the right of ra with intersection not empty
                newra=ens(self.start+self.offset,ra.end+self.offset)
                ra.end=self.start-1
                return newra,
        else:
            if self.end<ra.start: # disjoint
                return ens(0,-1),
            elif self.end>=ra.end: # ra included in self
                newra=ens(ra.start+self.offset,ra.end+self.offset)
                ra.end=ra.start-1
                return newra,
            else: # self to the left of ra with intersecption not empty
                newra=ens(ra.start+self.offset,self.end+self.offset)
                ra.start=self.end+1
                return newra,
        
            
def printm(lmap):
    for i in lmap:
        i.print()
        
        
f=open('input.txt')

lseed=[]
l=list(map(lambda i: int(i),f.readline().split(':')[1].split()))
for i in range(0,len(l),2):
    lseed.append(ens(l[i],l[i]+l[i+1]-1))
    
for i in lseed:
    i.print()
    
print(len(lseed))
for l in f:
    print(l)
    if l!='\n':
        l=l.split()[0].split('-')
        source=l[0]
        destintion=l[2]
        lmap=[]
        while True:
            l=f.readline()
            if l=='\n' or l=='':
                break
            else:
                l=l.split()
                lmap.append(maps(int(l[1]), int(l[1])+int(l[2])-1, int(l[0])-int(l[1])))
                
        printm(lmap)
        printm(lseed)
        print()
        nextseed=[]
        for i in lseed:
            if i.start > i.end:
                continue
            #i.print()
            for j in lmap:
                l=j.propagate(i)
                if len(l)==2:
                    lseed.append(l[1])
                if l[0].start<=l[0].end:
                    #print('c',i.start,i.end)
                    nextseed.append(l[0])
                if i.start>i.end:
                    break
            if i.start<=i.end:
                nextseed.append(i)
        lseed=nextseed
                

print('lseed')
printm(lseed)
mi=lseed[0].start
for i in lseed:
    mi=min(mi,i.start)
    
print(mi)
#print(lseed)
#print(min(lseed))