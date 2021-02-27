print("Введите строку:\n")
word = str(input())
word.split()


def new_func(word):
	print("\n\n")

	for i in word.split():
		print(str(i) + " - " + str(len(i)))

new_func(word)
