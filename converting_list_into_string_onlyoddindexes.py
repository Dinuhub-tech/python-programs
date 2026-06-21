l=["a","b","e","c","f"]
i=0
arr=[]
while i<len(l):
  if i%2==0:
    arr.append(l[i])
  i+=1
print(arr)
print("".join(arr))  ##converts list into string
