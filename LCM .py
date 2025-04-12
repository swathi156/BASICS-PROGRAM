n1 = 5
n2 = 20

lcm = min(n1, n2)  

while True:
    if lcm % n1 == 0 and lcm % n2 == 0:  
        print("LCM:", lcm)
        break 
    lcm=lcm+1
