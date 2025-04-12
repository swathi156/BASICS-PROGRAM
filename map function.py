def func(st):
    
    return st.upper()
ob=func("india")
print("answer",ob)
arr=["asia","italy"]
s=map(func,arr)
print(list(s))
