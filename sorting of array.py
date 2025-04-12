arr=[1,0,7,2]
n=arr[0]
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
       if arr[i]>arr[j]:
        arr[i],arr[j]=arr[j],arr[i]
for i in range(0,len(arr)):
   print(arr[i])
