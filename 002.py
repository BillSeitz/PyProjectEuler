# sum of even-valued Fibonacci terms that are under 4M
sum = 0
prev = 1
i = 1
while i < 4000000:
  # update sum
  if i % 2 == 0:
    sum = sum + i
  # generate next item
  new = prev + i
  prev = i
  i = new
  print i
print 'sum= ', sum
  
