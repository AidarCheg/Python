print("Ведите положительное четырехзначное число:")
n = int(input())

a = n // 1000
b = n // 100 % 10
c = n // 10 % 10
d = n % 10

print("\n\n" + str(a) + " - Thousands\n")
print(str(b) + " - Hundreds\n")
print(str(c) + " - Tens\n")
print(str(d) + " - Ones\n")