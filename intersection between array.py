n1 = [4,9,5]
n2 = [9,4,9,8,4]
m = []

for i in range(len(n1)):
    for j in range(len(n2)):
        if n1[i] == n2[j]:
            m.append(n1[i])
            k=set(m)
            p=list(k)
print(p)
