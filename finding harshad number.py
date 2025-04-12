n = 19
s = 0
m=n
while n>0:
    r=n%10
    s=s+r
    n=n//10
if m % s == 0:
    print("Harshad number")
else:
    print("Not a harshad number")
