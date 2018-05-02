inital = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
cal = []
final = []
for i in range(1,21):
  #print(inital)
  cal.append(1)
  for j in range(1,21):
    cal.append(cal[j-1] + inital[j])
  print(cal)
  inital = cal
  cal = []

'''

Revised method using permutation/combination

import math

a = math.factorial(40)
b = math.factorial(20)

# print "factorial of 40 =", a;
# print "factorial of 20 =", b;

print a / (b * b)

'''