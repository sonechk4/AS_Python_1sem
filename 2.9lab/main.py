with open('m.txt','w') as f:
    f.write('2 2 2\n1 -3\n-2 4\n\n5 -7\n-6 8\n')
with open('m.txt') as f:
    k, m, n = map(int, f.readline().split())
    mats = []
    cur = []
    for l in f:
        if l.strip():
            cur.append(list(map(int,l.split())))
            if len(cur) == m:
                mats.append(cur)
                cur = []

odd_mats = []
res = []
s = 0
for mat in mats:
    for strk in mat:
        for x in strk:
            if x<0 and x%2 != 0:
                s += x
    if s%2 != 0:
        odd_mats.append(mat)
        edinich = []
        for i in range(m):
            row = []
            for j in range(n):
                if i == j:
                    row.append(1)
                else:
                    row.append(0)
            edinich.append(row)
        res.append(edinich)
    else:
        res.append(mat)

with open('odd.txt','w') as g:
    for mat in odd_mats:
        for r in mat:
            g.write(' '.join(map(str, r))+'\n')
        g.write('\n')

with open('mod.txt','w') as h:
    for mat in res:
        for r in mat:
            h.write(' '.join(map(str, r))+'\n')
        h.write('\n')

print('исходный файл с изменениями:')
print(open('mod.txt').read())
print('файл с нечётными суммами:')
print(open('odd.txt').read())
