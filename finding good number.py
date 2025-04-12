n=int(input("Enter the input :"))
s=0
a=n
while(n>0):
    r=n%10
    s=s+r
    n=n//10
print("sum",s)    
if a%s==0:
    print("good number")
else:
    print("not a good number")




   
