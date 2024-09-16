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

result=0
with open('input.txt') as f:
    for l in f:
        l=l.split(',')
        for i in l:
            result+=hash1(i)
print(result)    