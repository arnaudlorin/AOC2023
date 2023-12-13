# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 08:25:01 2023

@author: artan
"""

import time

def sort_q(l):
    out=[l[i] for i in range(len(l))]
    index=[i for i in range(len(l))]
    for i in range(len(l)):
        maxi=out[i]
        max_index=i
        for j in range(i+1,len(out)):
            if out[j]>maxi:
                maxi=out[j]
                max_index=j
        out[max_index]=out[i]
        out[i]=maxi
        a=index[max_index]
        index[max_index]=index[i]
        index[i]=a
    return out,index

def maxi(l):
    maxi=l[0]
    maxi_index=[0]
    for i in range(len(l)):
        if maxi<l[i]:
            maxi=l[i]
            maxi_index=[i]
        elif maxi==l[i]:
            maxi_index.append(i)
    maxi_index=maxi_index[len(maxi_index)//2]
    return maxi,maxi_index

def explore(l,ldam,ind):
    #print(ind,l,ldam)
    if ldam==[]:
        find=False
        for i in l:
            if '#' in i:
                find=True
                break
        if not find:
            return 1
        else: 
            return 0
    if l==[]:
        return 0
    to_insert=ldam[0]
    data=l[0]
    remain=l[1:]
    icc=0
    #first try to add a .
    if data[0]=='?':
        if len(data)==1:
            icc+=explore(remain,ldam,ind+'.  ')
        else:
            icc+=explore([data[1:]]+remain,ldam,ind+'. ')
    #print(ind,l,ldam)
    #Then try to add data #
    if len(data)<to_insert:
        icc+=0
    elif len(data)==to_insert:
        icc+=explore(remain,ldam[1:],ind+'  ')
    elif data[to_insert]=='?': # Have to add a dot at the end, check if possible
        if len(data)==to_insert+1:
            icc+=explore(remain,ldam[1:],ind+'  ')
        else:
            icc+=explore([data[to_insert+1:]]+remain,ldam[1:],ind+'  ')

    return icc
    

def check(l,p,n):
    if l[p-1]=='#':
        return 0
    if l[p+n]=='#':
        return 0
    a=l[:p-1]
    b=l[p+n+1:]
    if a!=[]:
        a=[a]
    if b!=[]:
        b=[b]
    return(a,b)

def check_b(l,n):
    if l[n]=='#':
        return 0
    a=l[n+1:]
    if a==[]:
        return []
    else:
        return([a])

def check_e(l,n):
    if l[-n-1]=='#':
        return False
    a=l[:-n-1]
    if a==[]:
        return []
    else:
        return([a])



def explore_ord(l,ldam,ind):
    #print(ind,l,ldam)
    if ldam==[]:
        find=False
        for i in l:
            if '#' in i:
                find=True
                break
        if not find:
            return 1
        else: 
            return 0
    if l==[]:
        return 0
    
    to_insert,to_insert_index=maxi(ldam)
    possibility=[]
    for i in range(len(l)):
        if len(l[i])>=to_insert:
            possibility.append(i)
    result=0
    for i in possibility:
        
        if len(l[i])==to_insert:
            #print('b')
            out=explore_ord(l[:i],ldam[:to_insert_index],ind+'l ')
            out*=explore_ord(l[i+1:],ldam[to_insert_index+1:],ind+'r ')
            result+=out

        else:
            #print(ind,'a',result)
            test=check_e(l[i],to_insert)
            if test!=False:
                out=explore_ord(l[:i]+test,ldam[:to_insert_index],ind+'l ')
                if out!=0:
                    out*=explore_ord(l[i+1:],ldam[to_insert_index+1:],ind+'r ')
                    result+=out
                        
                        
            #print(ind,'c',result)
            test=check_b(l[i],to_insert)
            if test!=False:
                out=explore_ord(l[:i],ldam[:to_insert_index],ind+'l ')
                if out!=0:
                    out*=explore_ord(test+l[i+1:],ldam[to_insert_index+1:],ind+'r ')
                    result+=out
                    #print(ind,out,'resultc',result)
            
            
            for j in range(1,len(l[i])-to_insert):
                #print('j=',j,l[i],to_insert)
                test=check(l[i], j, to_insert)
                if test!=False:
                    out=explore_ord(l[:i]+test[0],ldam[:to_insert_index],ind+'l ')
                    if out==0:
                        continue
                    else:
                        out*=explore_ord(test[1]+l[i+1:],ldam[to_insert_index+1:],ind+'r ')
                        result+=out

    
   
    return result 

begin=time.time()
result=0
icc=0
f=open('input.txt')
for l in f:
    icc+=1
    broken_input=l.split()[0]
    broken_input=((broken_input + '?') *5)[:-1]
    broken_input= broken_input 
    group=''
    lgroup=[]
    for i in broken_input:
        if i=='#' or i=='?':
            group+=i
        elif group!='':
            lgroup.append(list(group))
            group=''
    if group!='':
        lgroup.append(list(group))
    damaged=list(map(lambda x:int(x),l.split()[1].split(',')))
    damaged=damaged*5
    print(icc)
    print(broken_input)
    print(damaged)
    a=explore_ord(lgroup,damaged,'')
    print(a)
    print()
    result+=a
end=time.time()
print(result)
print(end-begin)