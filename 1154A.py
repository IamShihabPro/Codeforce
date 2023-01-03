a= list(map(int, input().split()))
a.sort()
print(str(a[3]-a[2])+" "+str(a[3]-a[1])+" "+str(a[3]-a[0]))