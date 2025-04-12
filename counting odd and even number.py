arr=[1,2,3,4,5,6]
o=0
e=0
for i in range(len(arr)):
    if arr[i]%2==0:
        e=e+1
    else:
        o=o+1
print("even count",e)
print("odd count",o)
