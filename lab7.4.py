def reverse():
    x = int(input())
    if x != 0:
        reverse()
    print(x, end=" ")

print("Введите числа, 0 - для завершения ввода:")
reverse()