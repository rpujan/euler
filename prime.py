# break operator
# prime numbers
count = 0
for n in range(2, 100000):
  for x in range(2, int(round(n/2))):
    if n % x == 0:
      # print(n, 'equals', x, '*', n/x)
      break
  else:
      # loop fell through without finding a factor
    # print(n, 'is a prime number')
    count = count + 1

print(count)
