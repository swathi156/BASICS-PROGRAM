arr=[1,2,3,4]
d=0
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        c=arr[i]+arr[j]
        if c%2==0:
            print(arr[i],arr[j])   
            d=d+1
print("count",d) 
