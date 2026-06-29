x=eval(input())
for i in range(len(x)):
  for j in range(i+1,len(x)):
    if x[i]<x[j]:
      break
  else:
    print(x[i])
