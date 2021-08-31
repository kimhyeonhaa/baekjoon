# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 10:29:20 2020

@author: heena
"""

n=int(input())
dp=[0 for _ in range(n+1)]

for i in range(2,n+1):
    dp[i]=dp[i-1]+1
    if i%2==0 and dp[i]>dp[i//2]+1:
        dp[i]=dp[i//2]+1
    if i%3==0 and dp[i]>dp[i//3]+1:
        dp[i]=dp[i//3]+1
        
print(dp[n])