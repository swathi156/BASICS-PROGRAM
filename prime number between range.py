l = 10
u = 20
sum1 = 0

for i in range(l, u + 1):
    c = 0
    for j in range(1, i + 1):
        if i % j == 0:
            c += 1
    if c == 2:  
        sum1 += i

print("Sum of prime numbers:", sum1)
