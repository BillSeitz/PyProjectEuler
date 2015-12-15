# Find the sum of all the multiples of 3 or 5 below 1000.

from __future__ import division
sum = 0
i = 3
while i<1000:
  if (i/3 == int(i/3)) or (i/5 == int(i/5)):
    sum = sum + i
  i = i + 1
print sum

