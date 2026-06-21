arr = list(map(int, input().split()))

for i in arr:
    print(i,"=",arr.count(i),end=" ")

WITHOUT REPITITION
arr = list(map(int, input().split()))

for i in set(arr):
    print(i,"=",arr.count(i),end=" ")
