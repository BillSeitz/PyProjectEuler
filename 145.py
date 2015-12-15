# How many reversible numbers are there below one-billion (10^9)?
"""
Approach:
* generate for small number
* look for patterns in counts that can be extended
** 120 in first 1000 (120)
** 240 in first 2000 (120)
** 360 in first 3000 (120)
** 450 in first 4000 (90)
** 540 -> 90
** 600 -> 60
** 660 -> 60
** 690 -> 30
** 720 -> 30
** 720 in first 10000 - 0 more!
** 720 in 20000
** 720 in 50000
** 720 in 100,000
** 1920 in 120,000
** 13,320 in 500,000
** 18,720 at 899k
** 18,720 in 1,000,000
** 68,720 in 10,000,000 (at 9,894,808)
** 176,720 in 20,000,000 (at 19,990,008)
** ratio i/found keeps bouncing, up as high as 150 but eventually swings 99-109
** 446,720 in 50,000,000 (at 49,990,005) (ratio=111)
** interesting to watch the diff-between-sequentials run
** 99,999,999: 608720 89990001 ratio=147 diff=9000
"""

def is_all_odd(s):
  for c in s:
    n = int(c)
    if n % 2 == 0:
      return False
  return True

found = 608720
prev = 0
i = 99999998
while (i < 110000000):
  if i % 10 != 0: # ends with 0 so can't be used
    s = str(i)
    rs = s[::-1]
    r = int(rs)
    sum = i + r
    ssum = str(sum)
    #print s, rs, ssum
    if is_all_odd(ssum):
      found = found+1
      print '***', found, i, i/found, i-prev
      prev = i
    else:
      print i, found, i-prev
  i = i+1
      
    
