# What is the first term in the Fibonacci sequence to contain 1000 digits?
prev = 1
val = 1
i = 2
while (len(str(val))<1000):
  i = i+1
  new = prev+val
  print i, new
  prev = val
  val = new
