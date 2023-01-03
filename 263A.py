for col in range (1,6):
      row= list(map(int,input().split()))
      if 1 in row:
            x= row.index(1)+1
            y=col
print(abs(x-3)+abs(y-3))