# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 14:21:49 2023

@author: artan
"""


# Choose a node to be tested
def choose_node(node_out,d):
    mini=d[node_out[0]]
    index=node_out[0]
    for i in node_out:
        if d[i]<mini:
            mini=d[i]
            index=i
    return index


# Give the neighbor of the point next_node with direction d
def neighbor(next_node,n,d):
    l=[]
    dd=[]
    remain=next_node%n
    q=next_node//n
    if d==1 or d==3:
        for i in range(1,4):
            if remain+i>n-1:
                break
            l.append(q*n+remain+i)
            dd.append(0)
        for i in range(1,4):
            if remain-i<0:
                break
            l.append(q*n+remain-i)
            dd.append(2)
    elif d==0 or d==2:
        for i in range(1,4):
            if q+i>n-1:
                break
            l.append((q+i)*n+remain)
            dd.append(1)
        for i in range(1,4):
            if q-i<0:
                break
            l.append((q-i)*n+remain)
            dd.append(3)
    return l,dd

# Update the weight of node i, coming from next_node
def update_distance(next_node,i,distance,weight,d0,d):
    local=0
    if d==0:
        for j in range(1,i-next_node+1):
            local+=weight[next_node+j]
    elif d==2:
        for j in range(1,next_node-i+1):
            local+=weight[next_node-j]
    elif d==1:
        for j in range(1,(i-next_node)//n+1):
            local+=weight[next_node+j*n]
    else:
        for j in range(1,(next_node-i)//n+1):
            local+=weight[next_node-j*n]
            
    if distance[i+d*n**2]>distance[next_node+d0*n**2]+local:
        distance[i+d*n**2]=distance[next_node+d0*n**2]+local
        
def dijkstra(node_in,n,m,node_out,distance,weight):
    d=0
    while distance[n**2-1]==10*n*m or distance[2*n**2-1]==10*n*m:
        next_node=choose_node(node_out,distance)
        node_out.remove(next_node)
        node_in.append(next_node)
        d=next_node//n**2
        next_node=next_node%n**2
        neigh,dd=neighbor(next_node,n,d)
        for i in range(len(neigh)):
            update_distance(next_node,neigh[i],distance,weight,d,dd[i])
            
mat=[]
with open('input.txt') as f:
    m=0
    for l in f:
        m+=1
        l=l.split()[0]
        mat.append(list(map(lambda x:int(x),l)))

n=len(mat)
weight=[]
for i in mat:
    print(i)
    weight+=i

print('Start')
distance=[10*n*m for _ in range(4*n*m)]
distance[0]=0
distance[n**2]=0
node_out=[i for i in range(4*n*m)]
dijkstra([], n,m, node_out, distance, weight)

print(distance[n**2-1+n**2*0],distance[n**2-1+n**2*1])

 