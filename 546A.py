k,n,w = map(int,input().split())
c= 0
for i in range (1,w+1):
    c = c+i*k    # 1k+2k+3k...+wk it is the total cost of banana per (k doller)
b = c-n
if b<0:
    b=0
print(b)