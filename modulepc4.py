def if1(x):
	if x >= 1 and x <= 3:
		s = input("Введите строку = ")
		n = int(input("Введите количество повторов строки = "))
		a = [s for i in range(n)]
		for i in a:
			print(i)

def if2(x):
	if x >= 4 and x <= 6:
		m = int(input("Введите степень = "))
		x = x ** m
		print(x)

def if3(x):
	if x >= 7 and x <= 9:
		a = [i + x for i in range(10)]
		for i in a:
			print(i)

def else1(x):
	if x >= 1 and x <= 3:
		if1()
	if x >= 4 and x <= 6:
		if2()
	if x >= 7 and x <= 9:
		if3()
	else:
		print("\nОшибка ввода!!!\n")