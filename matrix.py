n1=int(input("enter row:"))
n2=int(input("enter col:"))
mat=[]
print("enter elements :")
for i in range(n1):
    a=[]
    for j in range(n2):
        a.append(int(input()))
    mat.append(a)
    

for i in range(n1):
    for j in range(n2): 
        print(mat[i][j],end="  ")
    print()           
