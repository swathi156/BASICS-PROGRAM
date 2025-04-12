
def func(st):
    c=0
    for i in range(len(st)):
     if st[i] in ['a','e','i','o','u']:
       
        c=c+1
    if c>0:
      print("vowel is present and count is",c)        
    else:
      print("no vowels")  
    return c
ob=func("apple")  
