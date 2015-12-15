# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
sum = 0
sum_sq = 0
for i in range(1,101):
  sum_sq = sum_sq + i*i
  sum = sum + i
sq_sum = sum * sum
diff = sq_sum - sum_sq
print sq_sum, sum_sq, diff

