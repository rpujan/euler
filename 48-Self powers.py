'''
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
'''

total = 0
def power(num):
  sum = 1
  for i in range(1, num+1):
    sum = sum * num
  return sum

for i in range(1,1001):
 total = total + power(i)

print(10,total) 
