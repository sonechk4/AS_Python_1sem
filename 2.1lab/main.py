"Пункт а"
keys = ['a', 'b', 'c']
values = [1, 2, 3]
res = dict(zip(keys, values))

"Пункт б"
items = [{'name': 'item1', 'price': 10},
         {'name': 'item2', 'price': 800},
         {'name': 'item3', 'price': 90},
         {'name': 'item4', 'price': 78}
]
sorted_items = sorted(items, key=lambda x: x['price'], reverse=True)
print(sorted_items[:3])

"Пункт в"
slov = [{'a': 1}, {'b': 2}, {'c': 3}]
ubrat = {'a': 1}
resc = []
for s in slov:
  if s != ubrat:
    resc.append(s)
print(resc)
