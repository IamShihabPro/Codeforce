n=int(input())
ans="I hate"
hate=" that I hate"
love=" that I love"
for i in range(2,n+1):
    if i%2==0:
        ans+=love
    if i%2!=0:
        ans+=hate
print(ans+" it")  