# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 11:27:05 2024

@author: artan
"""


class node:
    def ___init__(self,name,vertices):
        self.name=name
        self.vertices=vertices
        
def fac(n):
    if n==1: return 1
    return fac(n-1)*n


def maxi(l):
    ma=l[0]
    maxi=0
    for i in range(1,len(l)):
        if ma<l[i]:
            ma=l[i]
            maxi=i
    return maxi

def mincutst1(graph,weight,e):
    a=graph.pop()
    A={a}
    l=[weight[a][j] for j in e[a]]
    for i in range(len(graph)):
        a=maxi(l)
        l[a]=0
        A.add(a)
        for j in e[a]:
            l[j]+=weight[j][a]

def mincutst(graph,adj):
    a=0
    A={a}
    l=[0 for _ in range(len(graph))]
    for j in graph:
        l[j]=adj[a][j]
    for i in range(len(adj)-3):
        a=maxi(l)
        l[a]=0
        A.add(a)
        for j in graph-A:
            l[j]+=adj[j][a]
    s=maxi(l)
    l[s]=0
    A.add(s)
    for j in graph-A:
        l[j]+=adj[j][s]
    t=(graph-A).pop()
    return [[s,t],max(l)]
    
            
def cuts(graph,adj,merge):
    print(len(graph))
    if len(graph)==2:
        print('a',merge)
        return [adj[0][1],merge[0]]
    cut=mincutst(graph,adj)
    s=min(cut[0][0],cut[0][1])
    t=max(cut[0][0],cut[0][1])
    result=[cut[1],merge[cut[0][1]]]
    merge[s]+=merge.pop(t)
    l=adj.pop(t)
    for i in range(len(l)):
       # if i==t:
       #     continue
   
        adj[s][i]+=l[i]
    for i in adj:
        el=i.pop(t)
        i[s]+=el
    adj[s][s]=0

    graph.remove(len(graph)-1)
    
    return cuts(graph,adj,merge)+result
    
           
def add_nodes(l,e,graph):
    for i in l:
        if i in graph:
            graph[i]+=e.copy()
        else:
            graph[i]=e.copy()

graph={}
with open('input.txt') as f:
    for l in f:
        [start,end]=l.split(':')
        end=end.split()
        add_nodes([start],end,graph)
        add_nodes(end, [start], graph)
        
print(graph)
icc=0

for i in graph:
    print(i,len(graph[i]),graph[i])
    print()
    icc+=len(graph[i])
print()

conv={}
i=0
for e in graph:
    conv[e]=i
    i+=1

n=len(graph)
f=graph
graph={i for i in range(n)}
adj=[[0 for _ in range(n)] for _ in range(n)]
for i in f:
    for j in f[i]:
        adj[conv[i]][conv[j]]=1
        
for i in adj:
    print(i)
e={}
for i in f:
    e[conv[i]]={conv[j] for j in f[i]}
    
print()
l=[1 for _ in range(n)]
a=cuts(graph, adj,l)
mini=0
minv=a[0]
for i in range(len(a)//2):
    if a[2*i]<minv:
        minv=a[2*i]
        mini=i
print(a)
print(a[2*mini],a[2*mini+1],n-a[2*mini+1],a[2*mini+1]*(n-a[2*mini+1]))