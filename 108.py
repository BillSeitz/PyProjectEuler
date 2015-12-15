# What is the least value of n for which the number of distinct solutions exceeds one-thousand? (for 1/x + 1/y = 1/n)
""" Approach
* start with a decent-sized number n
* start stepping up from x=n+1 (we know that both x and y must be greater than n)
* calculate y, flag if win
* know to stop looking when....?
** y=n+1?
** x=y0?
** duh, for distinct, stop at x=2*n

Examples: 
* 120: 32
* 180: 38
* 210: 41
* 360: 53
* 420: 68 (up to here these are *consecutive* max cases)
* 9240: 283
* 18480: 361 (having started at 420x10)
* 27720 has 462 matches
* 32760: 468 (this was still max at n=45246) (repeated when started from 420)
* *** starting over in this range****
* 100,050: 183 (relaunched starting at 100k)
* 100,100: 317
* 180,180: 945 (from launch 45200, by 10) (still true at 223300)
* 200,200: 429 (relaunched starting at 200k) (still true at 200,500) (still true until 240240!)
* 200,970: 544 (relaunched starting at 200,500, jumping by 10)
* 205,920: 683
* 207,480: 769
* 235620: 922
* 240240: 1006 **** but rejected! Maybe I missed an earlier case?
* new cases with new reciprocal formula!
* earlier numbers match!
* 1st place (n,x,y) where 2 methods disagree: 220, 221, 48620
* 120, 180, 210, 360, 420 all match earlier values
* 840: 95
* 1260: 113
* 9240: 284 - not match!
* 18480: 365 - not match!
* 27720: 473 (up to 41540)
* 32760: 473 (up to 45940)
* 64020: 203
* 64260: 473
* 65520: 608 (up to 70370)
* 78540: 608
* 83160: 662 (up through 109900)
* 110880: 743
* 120120: 851 (up through 177000)
* 180000: 284
* 180180: 1013 (starting from 120120) (rejected!)
* 240240: 1094
"""

from __future__ import division

def is_whole(n): #is this a whole number?
  if abs(n - round(n)) < 0.000000001: return True 
  else: return False

def is_solution(n, x, y): # do these 3 numbers work? Use reciprocal to avoid float error
  if n == (x*y)/(x+y): 
    #print 'is_sol: ', n, x, y, (x*y)/(x+y)
    return True
  else: 
    #print 'is_sol: n, x, y, 1.0 * (x*y)/(x+y): ', n, x, y, 1.0 * (x*y)/(x+y)
    return False

num_hits_latest = [0,0]
num_hits_max = [78540, 608] #[0,1]

# calculate theoretical max
#n=4
#while num_hits_latest[1] <= 8:
#  y0 = 1/(1/n - 1/(n+1))
#  num_hits_latest[1] = int(y0/n)
#  print n, num_hits_latest[1]
#  n = n+1
#num_hits_latest = [0,0]

n = 83020
while num_hits_max[1] <= 1000:
  num_hits_latest[1] = 0
  x = n + 1
  y0 = 9999999999
  x_last = 0
  y_last = 0
  while(x <= 2*n):
    y = 1/(1/n - 1/x)
    if is_solution(n, x, round(y)):
      num_hits_latest[0] = n
      num_hits_latest[1] = num_hits_latest[1] + 1
      #if not is_whole(y):
        #print '**disagree n, x, y, (x*y)/(x+y): ', n, x, y, (x*y)/(x+y)
        #pass
    else:
      #print 'n, x, y, y-int(y), int(y), x_last, y_last', n, x, y, y-int(y), int(y), x_last, y_last
      pass
    x = x + 1
  if num_hits_latest[1] > num_hits_max[1]:
    num_hits_max[0] = n
    num_hits_max[1] = num_hits_latest[1]
  print '**num_hits_latest, max: ', num_hits_latest, num_hits_max, num_hits_max[0]/num_hits_max[1]
  n = n + 10
print '****num_hits_latest, max: ', num_hits_latest, num_hits_max


