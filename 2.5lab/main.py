def Simm(s, i, j):
    if i>=j:
        return True
    if s[i] == s[j]:
        return Simm(s, i+1, j-1)
    else:
        return False

print(Simm('казак', 0, 4))
