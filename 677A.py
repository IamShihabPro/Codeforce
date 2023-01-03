n,m = list(map(int,input().split()))
a= list(map(int,input().split()))
c=0
for i in range (n):
    if a[i]<=m:
        c+=1
    elif a[i>m]:
        c+=2
print(c)