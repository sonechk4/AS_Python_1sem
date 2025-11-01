# Дано положительное целое число N. Найти наибольшее целое число K, квадрат которого не превосходит N: K^2≤N.
n = int(input())
maxk = 0
for k in range(1, n):
  if k**2 <= n:
    maxk = max(k, maxk)
print(maxk)
