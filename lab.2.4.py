year = int(input())
2021
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
 print(str(year) + ' Високосный год')
else:
 print(str(year) + ' НЕ високосный год')
