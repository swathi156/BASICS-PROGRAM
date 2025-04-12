arr=[1,1,2,3,3,4]
a=[]

for i in arr:
    if arr.count(i)==1:
        a.append(i)
print(a)
