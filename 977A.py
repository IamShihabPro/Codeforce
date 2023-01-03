n,k= map(int,input().split())
for i in range (k):
    x=n%10
    if (x==0):
        n//=10
    else:
        n-=1
print(n)
            