# 2231.py

n=input()

l=len(n)
if l==1 or l==2:
    num=0
else:
    num=int(n)-l*10

for i in range(num,int(n)+1):
    result=num+sum(map(int,str(num)))
    if result==int(n):
        print(num)
        break
    num+=1
    
if int(n)==num-1:
    print(0)
    
'''
while int(n)!=num:
    result=num
    for i in num_str:
        result+=int(i)
    if result==int(n):
        print(num)
        break
    num+=1
    num_str=str(num)
    
if int(n)==num:
    print(0)
'''