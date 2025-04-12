n=6
s=0
for i in range(1,n):
    if n%i==0:
        s=s+i
    
    print("val is",i,"sum is",s)   
       
if s==n:
    print("perfect number")
else:
    print("not perfect number")  

