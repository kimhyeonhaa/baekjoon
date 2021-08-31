# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 10:45:17 2020

@author: heena
"""

import math

min,max=map(int,input().split())
count=max-min+1
for i in range(min,max+1):
    for j in range(2,int(math.sqrt(i))+1):
        if i%(j*j)==0:
            count-=1
            break
print(count)