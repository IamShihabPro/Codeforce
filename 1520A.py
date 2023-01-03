t = int(input())
for i in range (t):
    n = int(input())
    s= input()
    temp= s[0]
    new = [temp]
    count=1
    while count<n:
        if temp!=s[count]:
            if s[count] in new:
                print("NO")
                break
            else:
                new.append(temp)
                temp=s[count]
        count+=1
    else:
        print("YES")
