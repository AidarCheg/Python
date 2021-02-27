print("Введите элементы в список:\t")

s=input()
a=[int(s) for s in s.split()]

print("Четные элементы списка:\t")

for i in a:
    if int(i)%2 == 0:
       print(i, end=' ')