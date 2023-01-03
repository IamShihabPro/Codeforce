n = int(input())
c=1
v=1
a= list(map(int, input().split()))
for i in range (n-1):
    if a[i]<=a[i+1]:
        c+=1
    else:
        v=max(v,c)
        c=1
print(max(v,c))