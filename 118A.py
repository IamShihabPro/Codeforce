v=['a','o','y','e','u','i']
s=''
txt = str(input())
k= txt.lower()
for i in range(len(txt)):
    if k[i] not in v:
        s+='.'
        s+=k[i]
print(s)
