# python program to find factorial of a number provided by the user

def fact(num):
  factorial = 1
  if num < 0:
    print("sorry, factorial does not exist for negative numbers")
  elif num == 0:
    print("The factorial of 0 is 1")
  else:
    for i in range(2, num + 1):
      factorial = factorial * i 
    print("The factorial of", num, "is", factorial)

fact(1000)
