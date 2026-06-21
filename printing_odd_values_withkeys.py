l=["a","b","e","c","f"]
d={}
for i in range(len(l)):
  d[l[i]]= i
print(d)
arr1=[]
arr2=[]
for k,v in d.items():
  if v%2!=0:
    arr1.append(k)
    arr2.append(v)
print(arr1)
print(arr2)
