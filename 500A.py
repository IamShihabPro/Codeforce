a,b=list(map(int,input().split()))
l=list(map(int,input().split()))
dic={}
for i in range(1,a):
    dic[i]=i+l[i-1]
a=1
while True:
    if a not in dic:
        print('NO')
        break
    else:
        a=dic[a]
    if a==b:
        print('YES')
        break