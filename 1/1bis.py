# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 09:44:25 2023

@author: artan
"""

import re


def convert(s):
    if s=='one' or s=='eno':
        return 1
    elif s=='two' or s=='owt':
        return 2
    elif s=='three' or s=='eerht':
        return 3
    elif s=='four' or s=='ruof':
        return 4
    elif s=='five' or s=='evif':
        return 5
    elif s=='six' or s=='xis':
        return 6
    elif s=='seven' or s=='neves':
        return 7
    elif s=='eight' or s=='thgie':
        return 8
    elif s=='nine' or s=='enin':
        return 9
    else:
        print(s)
        return int(s)
    
p=re.compile('\d|one|two|three|four|five|six|seven|eight|nine')
q=re.compile('\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin')
f=open("input.txt")
tot=0
for l in f:
    l=l.split()[0]
    k=''
    for i in l:
        k=i+k
    print(l,k)
    res=p.findall(l)
    res2=q.findall(k)
    a=convert(res[0])
    b=convert(res2[0])
    print(res,a,res2,b,10*a+b)
    tot+=10*a+b
print(tot)