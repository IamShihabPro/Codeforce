s= str(input())
l ='hello'
c=0
for i in range (len(s)):
    if s[i]==l[c]:
        c+=1
        if (c==5):
            break
if c==5:
    print("YES")
else:
    print("NO")