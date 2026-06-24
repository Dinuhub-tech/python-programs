def fact(r):
  fact=1
  while r>=1:
    fact*=r
    r-=1
  return fact
n=int(input("No. of people"))
r=int(input("no.of r seats"))
nr=fact(n)
dr=fact(n-r)
print(nr/dr)
