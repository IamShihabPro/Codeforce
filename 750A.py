n,k= map(int,input().split())
c=0
k=240-k
l=[5,10,15,20,25,30,35,40,45,50,55]
for i in range (n):
    if k-l[i]>=0:
       c+=1
       k-=l[i]
print(c)
