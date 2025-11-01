# Дан список. Выбрать из списка все числа на нечетных позициях и упорядочить эти числа по убыванию.
import numpy as np
spisok = np.arange(1, 100)
res = []
for i in range(len(spisok)):
  if i%2 != 0:
    res.append(int(spisok[i]))
print(sorted(res, reverse=True))
