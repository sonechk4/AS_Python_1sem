# Дан список. Найти два соседних элемента, сумма которых максимальна, и вывести эти элементы в порядке возрастания их индексов.
import numpy as np
spisok = np.arange(1, 100)
maxs = 0
ind = 0
for i in range(len(spisok)-1):
  if spisok[i] + spisok[i+1] >= maxs:
    maxs = spisok[i] + spisok[i+1]
    ind = i
print(spisok[i], spisok[i+1])
