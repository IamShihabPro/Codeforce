s1=input()
s2=input()
c= len(s1)
l=[]
i=0
while(i<c):
    if s1[i]!=s2[i]:
        l.append(1)
    else:
        l.append(0)
    i+=1
print(*l,sep='')
