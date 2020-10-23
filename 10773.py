# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 14:33:33 2020

@author: heena
"""

N=int(input())
top=0

stack=[]
for i in range(N):
    a=int(input())
    if a==0:
        top-=1
        del stack[top]
        
    else:
        stack.append(a)
        top+=1
print(sum(stack))