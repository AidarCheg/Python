ma = int(input())
mi = int(input())
for cikl in range(ma - (ma + 1) % 2, mi - mi % 2, -2):
    print(cikl, end=' ')