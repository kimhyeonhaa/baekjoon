# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 00:16:54 2020

@author: heena
"""

n=int(input())
p=[0,1]
for i in range(2,n+1):
    p.append(p[i-1]+p[i-2])
print(p[n])