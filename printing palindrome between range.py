n=1000
o=1500


for i in range(n,o+1):
    m=i
    rev=0
    while i>0:
        r=i%10
        rev=(rev*10)+r
        i=i//10
    if rev==m:
        print("palindrome",m)
