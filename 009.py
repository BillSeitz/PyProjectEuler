# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Give product a*b*c.
import math
cmax = 1000
status = ''
for b in range(1,cmax):
  if status != '':
    break
  for a in range(1,b):
    c2 = a**2 + b**2
    c = math.sqrt(c2)
    if c == int(c): # we have a triplet
      print a, b, c
      if a+b+c == 1000:
        status = 'winner!', a*b*c
        print status
        break
