arr=list(map(int,input().split()))
smallest=arr[0]
for i in arr:
    if i <smallest:
        smallest=i
print(smallest)
