print("Доброго времени суток!")
print("Введите число от 1 до 9:")

val = int(input())

print("Входные данные:%.2f" % val)

if (1 <= val <= 3):
	print("Введите строку:")
	s = str(input())
	print("Число повторов строки:")
	n = int(input())
	i = 0
	while i < n:
		print (s)
		i = i + 1
elif (4 <= val <= 6):
	print("Введите степень:")
	m = int(input())
	print("Введите число x:")
	x = int(input())
	x = x**m
	print("Число в степени:%.2f" % x)
elif (7 <= val <= 9):
	print("Введите число x:")
	x = int(input())
	i = 0
	while i <=10:
		x =  x + 1
		i = i + 1
		print(x)
else:
	print("Ошибка ввода!")
