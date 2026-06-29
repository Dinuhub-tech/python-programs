x=eval(input())
for i in range(len(x)):
  for j in range(len(x)):
    if x[i]<x[j]:
      x[i],x[j]=x[j],x[i]
print(x)
for i in range(len(x)-1,-1,-1):
  if x[-1]!=x[i]:
    print(x[i])
    break
