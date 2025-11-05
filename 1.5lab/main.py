# Дан список. Выбрать из списка все числа на нечетных позициях и упорядочить эти числа по убыванию.
spisok = [1, 14, 12, 8, 10]
res = []
for i in range(len(spisok)):
  if i%2 != 0:
    res.append(spisok[i])
print(sorted(res, reverse=True))
