n = int(input())
for i in range (n):
    a,b= map(int, input().split())
    x= abs(a-b)
    c= x//10
    if x%10>=1 and x%10<=9:
        c+=1
    print(c)
 