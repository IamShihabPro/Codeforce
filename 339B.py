def path (start, data, num):
    if data >= start:
        return data-start
    else:
        return num + data - start
n,m= map(int,input().split())
a= list(map(int,input().split()))
count = 0
start = 1
for i in range (m):
    count+=path(start, a[i], n)
    start=a[i]
print(count)