def step(*args):
	stepen = 1
	for i in args:
		res = pow(i, stepen)
		stepen += 1
		print(str(res), end=' ')
	print("\n")
