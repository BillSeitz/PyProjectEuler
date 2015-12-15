# Find 2nd triplet of 4-dig numbers where the 3 numbers are permutations of each other, and all 3 are prime, and the diffs between the consecutive pairs is the same. Only other 4-dig triplet is: 1487, 4817, 8147 (each separated by 3330)
""" 
Approach:
* count up starting at 1000 (actually 1001, going up by 2)
* there are 24 permutations of any 4-dig number: test each for being >1000 and being prime
"""

global primes, winners # dictionary of numbers, and whether each is a prime
primes = {}
winners = []

import math
def is_prime(x):
  if x in primes:
    return primes[x]
  for i in range(2, int(math.sqrt(x))+1):
    if x % i == 0:
      primes[x] = False
      return False
    else: i = i+1
  primes[x] = True
  return True

def net(s, i): #return string s with digit i removed
  sn = ''
  for j in range(0, len(s)):
    if j != i:
      sn = sn + s[j]
  return sn

def lnet(s, i): #return list s with items-through-i removed
  sn = []
  #print 'lnet: ', s, i, range(0,len(s))
  for j in range(0, len(s)):
    if j > i:
      sn.append(s[j])
  #print 'lnet net: ', sn
  return sn
  
for i in range(1001,9999,2):
  si = str(i)
  si_orig = si
  
  # generate every permutation
  perms = [] # list of unique prime perms of i
  p = ['0','0','0','0'] # list of string-digits in permutation being created/tested
  for a in range(0,4):
    p[0] = si[a]
    sia = net(si, a)
    #print si_orig, sia, p
    for b in range(0,3):
      #print 'b=', b
      p[1] = sia[b]
      #print 'p=', p
      sib = net(sia, b)
      for c in range(0,2):
        #print 'c=', c
        p[2] = sib[c]
        sic = net(sib, c)
        p[3] = sic
        ps = ''.join(p)
        #print 'final p=', ps
        pn = int(ps)
        if pn < 1000: break
        if not is_prime(pn): break
        if pn not in perms: 
          perms.append(pn)
          #print 'perms: ', perms

  perms.sort() # note that diffs concept means will need ordered lists

  if len(perms) >= 3: # sets to test for diffs
    print '* 3+ prime permutations:', perms
    m_to_pick = len(perms)-2
    #print 'm-range: ', range(0, m_to_pick)
    for m in range(0, m_to_pick):
      subset = [0,0,0]
      subset[0] = perms[m]
      sub_m = lnet(perms, m)
      n_to_pick = len(sub_m)
      #print 'subset, sub_m, n-range: ', subset, sub_m, range(0, n_to_pick)
      for n in range(0, n_to_pick):
        subset[1] = sub_m[n]
        sub_n = lnet(sub_m, n)
        #print 'sub_n: ', sub_n
        q_to_pick = len(sub_n)
        #print 'q-range: ', subset, sub_m, sub_n, range(0, q_to_pick)
        for q in range(0, q_to_pick):
          subset[2] = sub_n[q] # now have a triple
          #subset.sort()
          #print 'testing subset: ', subset, sub_m, sub_n, m, n, q
          print 'testing subset: ', subset
          if (subset[2] - subset[1]) == (subset[1] - subset[0]):
            print '**** big winner: ', subset
            if subset not in winners:
              winners.append(subset)
print 'winning list: ', winners

            
