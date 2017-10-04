n=0
total=""
while True:
    n+= 1
    total += str(n)
    if(len(total) >= 1000000):
        break
    
multi = int(total[0]) * int(total[9]) * int(total[99]) * int(total[999]) * int(total[9999]) * int(total[99999]) * int(total[999999])
print multi