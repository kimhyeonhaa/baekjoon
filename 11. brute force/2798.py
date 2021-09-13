# 2798.py

n,m=map(int,input().split())
card=list(map(int,input().split()))

card_max=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            card_sum=card[i]+card[j]+card[k]
            if card_max<card_sum<=m:
                card_max=card_sum

print(card_max)