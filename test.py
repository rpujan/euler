import math

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

sp = 0
sum = 0
flag = False
for i in range(1,100):
    if is_prime(i):
        sum = sp
        sp += i        
        if is_prime(sp):
            #print(i,sp)
            flag = False
        else:
            if flag == True:
                break
            flag = True
print(sum)