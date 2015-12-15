# What is the largest prime factor of the number 600851475143 ?
""" Plan:
* start from i=3, go up by 2
* check if i divides in n
* if so, save i and start working with n/i
"""
import math
n = 600851475143
max_possible_factor = math.sqrt(n)
i = 3
max = 1
while i < max_possible_factor:
  if n % i == 0: # yes divides, not prime
    print i
    max = i
    n = n/i
  i = i+2
