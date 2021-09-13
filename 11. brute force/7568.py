# 7568.py

n=int(input())

weight=[]
height=[]
for i in range(n):
    a,b=map(int,input().split())
    weight.append(a)
    height.append(b)

result=[1 for i in range(n)]
for j in range(n-1):
    for k in range(j+1,n):
        if j!=k:
            if weight[j]>weight[k]:
                if height[j]>height[k]:
                    result[k]+=1
            if weight[j]<weight[k]:
                if height[j]<height[k]:
                    result[j]+=1

for i in result:
    print(i,end=' ')