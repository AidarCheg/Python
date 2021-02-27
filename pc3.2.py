x = int(input("Введите число от 1 до 10 = "))


def proverka(x):
	if x >= 1 and x <= 3:
		s = input("Введите строку = ")
		n = int(input("Введите количество повторов строки = "))
		a = [s for i in range(n)]
		for i in a:
			print(i)

	elif x >= 4 and x <= 6:
		m = int(input("Введите степень = "))
		x = x ** m
		print(x)

	elif x >= 7 and x <= 9:
		a = [i + x for i in range(10)]
		for i in a:
			print(i)
	else:
		print("Ошибка ввода")



print("Функция вызвана:")
proverka(x)
