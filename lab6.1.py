print("Введите элементы в массив(список):")
a = input().split()

print("Элементы с четными индексами:\t")
for i in range(0, len(a), 2):
    print(a[i], end=" ")