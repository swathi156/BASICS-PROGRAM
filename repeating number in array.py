arr=[1,3,2,1,4,3]
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
           print(arr[i])
