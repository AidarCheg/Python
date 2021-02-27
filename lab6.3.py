print("Введите элменты в список:\t")

a = [int(i) for i in input().split(" ")]

print("Результат:\t")

for i in range(1, len(a)):
    if a[i - 1] * a[i] > 0:
        print(a[i - 1], a[i])
        break