def Chessboard(m, n):
    res = []
    for x in range(m):
        row = []
        for y in range(n):
            if (x+y)%2 == 0:
                row.append(0)
            else:
                row.append(1)
        res.append(row)
    return res
matrix = Chessboard(3, 5)
print(matrix)
