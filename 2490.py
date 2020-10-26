s=[]
s.append(input().count('0'))
s.append(input().count('0'))
s.append(input().count('0'))

for i in s:
    if i==1:
        print('A')
    elif i==2:
        print('B')
    elif i==3:
        print('C')
    elif i==4:
        print('D')
    else:
        print('E')