n=145

m=0
p=n
while n>0:
    r=n%10
    f=1
    for i in range(1,r+1):
      f=f*i
    m=m+f
    print(m) 
    n=n//10
if m==p:
    print("given input is a strong number")
else:
    print("given input is not a strong number")        



   
