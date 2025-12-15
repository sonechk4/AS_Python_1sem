with open('f.txt', 'r') as f, open('g.txt', 'w') as g, open('h.txt', 'w') as h:
    numbers = f.read().split()
    for num in numbers:
        n = int(num)
        if n % 2 == 0:
            g.write(num + ' ')
        else:
            h.write(num + ' ')
