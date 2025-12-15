def LuckyNum(a):
    if (int(str(a)[0]) + int(str(a)[1])) == (int(str(a)[2]) + int(str(a)[3])):
        return True

for i in range(1000, 10000):
    if LuckyNum(i) == True:
        print(i)
