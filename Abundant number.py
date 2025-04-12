n=12
s=0
for i in range(1,n):
    if n%i==0:
       print("val is",i)   
       s=s+i
print("sum is",s)
if s>n:
    print("abundant number")
else:
    print("not a adundant number")    
