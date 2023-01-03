n, k = map(int, input().split())
a = list(map(int,input().split()))
c=0
temp = a[k-1]
for i in range (n):
    if a[i]>=temp and a[i]>0:
        c+=1
print(c)
