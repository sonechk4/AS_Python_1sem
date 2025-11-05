# Дан список. Найти два соседних элемента, сумма которых максимальна, и вывести эти элементы в порядке возрастания их индексов.
spisok = [1, 4, 12, 8, 10]
maxs = 0
ind = 0
for i in range(len(spisok)-1):
  if spisok[i] + spisok[i+1] >= maxs:
    maxs = spisok[i] + spisok[i+1]
    ind = i
print(spisok[ind], spisok[ind+1])
