n=int(input())
fact=1
if n==0:
    print("the factorial of 0 is 1")
elif n>0:
    for i in range(1,n+1):
        fact*=i
    print(fact)
else:
    print("enter positive number")
