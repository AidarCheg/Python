s = input('Введите строку:\t')

print("\nРезультат:\n")

s = s[:s.find('h')] + s[s.rfind('h') + 1:]
print(s)