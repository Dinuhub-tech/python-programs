x=eval(input())
arr1=[]
arr2=[]
for i in x:
  if i>0 or i<0:
    arr1.append(i)
  else:
    arr2.append(i)
arr1.extend(arr2)
print(arr1)
