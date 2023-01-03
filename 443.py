n= input()
l=[]
for i in n:
    if i!='{' and i!=',' and i!='}' and i!=" ":
        l.append(i)
print(len(set(l)))