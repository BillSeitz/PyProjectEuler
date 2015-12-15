# Find the largest palindrome made from the product of two 3-digit numbers.
max = 1
for i in range(999, 100, -1):
  for j in range(i, 100, -1):
    product = i * j
    s = str(product)
    s_rev = s[::-1]
    if s == s_rev:
      if s > max:
        print i, j, s
        max = s
