# s= str(input()).lower()
# k = len(s)
# if k<=3:
#     s=s.upper()
#     print(s)
# else:
#     print(s)

s= input()
cp=0
sm=0
for i in s:
    if i.isupper():
        cp+=1
    else:
        sm+=1
if cp>sm:
    print(s.upper())
else:
    print(s.lower())