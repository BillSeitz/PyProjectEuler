# How many starting numbers below ten million will arrive at 89? (by continuously adding the square of the digits in a number to form a new number until it has been seen before.)
"""
Approach
* take every number, go through its chain until hit 1 or 89
* count which one it hits
"""

def chain(n): # calculate next number in the chain for n
  s = str(n)
  total = 0
  for c in s:
    nc = int(c)
    nc2 = nc**2
    total = total + nc2
  if total in (1,89):
    counts[total] = counts[total] + 1
    return
  else:
    chain(total)

global counts
counts = {1:0, 89:0}
for i in range(1,10000002):
  chain(i)
  print i, counts
  
