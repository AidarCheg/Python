s=input('Введите строку:\t')

print("\nРезультат:\n")
first = s[:s.find(' ')]
second = s[s.find(' ') + 1 :]
print(second + ' ' + first)