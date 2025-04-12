def func(st):
    re=""
    for i in range(len(st)-1,-1,-1):
         re=re+st[i]
    if re==st:
          print("string is  palindrome")
    else:
          print("string is not a palindrome")                       
    return re          
ob=func("hi")
