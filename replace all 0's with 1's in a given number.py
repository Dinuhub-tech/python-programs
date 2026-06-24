n=int(input())
k=""
while n>0:
  r=n%10
  if r==0:
    k=str(1)+k
  else:
    k=str(r)+k
  n=n//10
print(k)
