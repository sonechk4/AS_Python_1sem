# Найти первый неповторяющийся символ в заданной строке.
strok = str(input())
for s in strok:
  if strok.count(s) == 1:
    print(s)
    break
