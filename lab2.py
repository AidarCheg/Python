import math

ab = input("Длина первого катета:")
ac = input("Длина второго катета:")

ab = float(ab)
ac = float(ac)

bc = math.sqrt(ab**2+ac**2)

s = (ab * ac) / 2
p = ab + ac + bc

print("Площадь треугольника:%.2f" % s)
print("Периетр треугольника:%.2f" % p)