n = int(input())
a= list(map(int, input().split()))
a.sort(reverse= True) # dec sorting process
c=0
v=0
s=sum(a)             # sum of all numbers in a list
while(v<=s//2):      # loops untill v <= s//2
    v+=a[c]          # value of v is a[0] index by looping
    c+=1             # count increse 1 
print(c)



