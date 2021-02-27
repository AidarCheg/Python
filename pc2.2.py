print("Введите знак для определения раздела:")
a = str(input())

print("Введите строку:")
f = str(input())

print(f.split(a))
print("Слова которые вы ввели:")
print(*map(lambda x: (len(x), x), f.split(a)))
s = max(map(lambda x: (len(x), x), f.split(a)))
print("Самое длинное слово:")
print (s)
print (s[1])