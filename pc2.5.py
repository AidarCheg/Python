print("\nВведите строку:")
f = str(input())

print("\n\nСлова которые вы ввели:\n\n")

count = 0
flag = 0

print(*map(lambda x: (len(x), x), f.split(" ")))

for i in range(len(f)):
	if f[i] != ' ' and flag == 0:
		count += 1
		flag = 1
	else:
		if f[i] == ' ':
			flag = 0

print("\n\nКоличесвто слов в строке:\t\t" + str(count))
