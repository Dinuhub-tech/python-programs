n=int(input())
arr=[]
for i in range(1,n+1):
  if n%i==0:
    arr.append(i)
for i in arr:
  if i>1:
    for j in range(2,i):
      if i%j==0:
        break
    else:
      print(i,end=" ")
