x=input()
y=input()
z=min(len(x),len(y))
count=0
for i in range(z):
  for j in range(i,i+1):
    if x[i]==y[j]:
      count+=1
print(count)
