arr=[1,1,2,3,3,4]
a=[]
s=0
for i in arr:
    if arr.count(i)==1:
        a.append(i)
for i in a:
    s=s+i
print("sum",s)

   








