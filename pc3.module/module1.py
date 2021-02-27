def if1(x):
	if x >= 1 and x <= 3:
		s = input("Введите строку = ")
		n = int(input("Введите количество повторов строки = "))
		a = [s for i in range(n)]
		for i in a:
			print(i)