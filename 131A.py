import string
n=int(input())
s=str(input())
a = "abcdefghijklmnopqrstuvwxyz"
for i in a:
    if i not in s.lower():
        print("NO")
        break
else:        
    print("YES")
