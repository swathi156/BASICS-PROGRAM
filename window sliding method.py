n1=int(input("enter window size:"))
arr=[1,2,3,1,2,4,1,2,6]

m=[]
for i in range(0,len(arr),n1):
    s=1
    r=arr[i:i+3]
    for j in r:
      s=s+j
    m.append(s)
    print("sum",s)    
   
print("m val",m)
k=m[0]
for i in m:
   if i < k:
      k=i
print("least sum",k)  

