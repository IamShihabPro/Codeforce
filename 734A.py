n = int(input())
a=0
d=0
s = input()
for i in range (n):
    k=s[i]
    if k=='A':
        a+=1
    else:
        d+=1
if a>d:
    print("Anton")
elif a<d:
    print("Danik")
else:
    print("Friendship")
    