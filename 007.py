# What is the 10001st prime number?
import math
def is_prime(x):
  for i in range(2, int(math.sqrt(x))+1):
    if x % i == 0:
      return False
    else: i = i+1
  return True
n = 1 # number of primes so far (first prime is 2)
i = 3 # candidate prime number
while n <= 10001:
  if is_prime(i):
    n = n+1
    print n, i
  i = i+2

