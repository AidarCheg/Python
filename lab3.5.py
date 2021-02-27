import math
print("Введите катеты треугольника:")
a = int(input())
b = int(input())
c = math.sqrt(b*b + a*a)

print("\nГипатенуза треугольника:\t"+str(c))