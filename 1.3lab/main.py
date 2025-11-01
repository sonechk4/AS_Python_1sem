# Для заданного натурального n и действительного x подсчитать сумму: 1 + x + x^2/2! + x^3/3! + ... + x^n/n!
import math
n = int(input())
x = float(input())
summ = 1
for k in range(1, n+1):
  summ += (x**k / math.factorial(k))
print(summ)
