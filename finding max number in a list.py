x=list(map(int,input().split()))
max=x[0]
for i in range(len(x)):
  if x[i]>max:
    max=x[i]
print(max)
