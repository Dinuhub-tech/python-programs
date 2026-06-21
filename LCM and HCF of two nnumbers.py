n1=int(input())
n2=int(input())

small=min(n1,n2)

for i in range(1,small+1):
    if(n1 % i==0 and n2 % i==0):
        hcf=i
print(hcf)
print((n1*n2)/hcf)
