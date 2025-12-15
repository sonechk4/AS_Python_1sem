with open("file.txt", "w") as f:
    f.write("Первая\nВторая\nТретья\nЧетвертая\n")
K = 2
with open("file.txt", "r") as f:
    lines = f.readlines()
if K <= len(lines):
    lines.insert(K - 1, "\n")
    with open("file.txt", "w") as f:
        f.writelines(lines)
with open("file.txt", "r") as f:
    print(f.read())
