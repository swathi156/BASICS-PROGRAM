arr = [2, 6, 4, 12, 8, 10]
m = len(arr) // 2
a1 = arr[:m]  
a2 = arr[m:]  
for i in range(len(a1)):
    for j in range(i + 1, len(a1)):
        if a1[i] > a1[j]: 
            a1[i], a1[j] = a1[j], a1[i]
print("ascen",a1)
for i in range(len(a2)):
    for j in range(i + 1, len(a2)):
        if a2[i] < a2[j]:
            a2[i], a2[j] = a2[j], a2[i]
print("desc",a2)
