n=int(input())
for i in range(n):
    s=input()
    sum=0
    k=0
    for j in s:
        if j=='O':
            k+=1
            sum+=k
        else:
            k=0
            sum+=k
    print(sum)