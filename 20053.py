# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 00:40:00 2020

@author: heena
"""

N=int(input())
minnum=[]
maxnum=[]
num=[]
for i in range(N):
    a=int(input())
    num=list(map(int, input().split()))
    maxnum.append(max(num))
    minnum.append(min(num))
for i in range(N):
    print(minnum[i],maxnum[i])