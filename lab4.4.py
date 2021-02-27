print('Введите количество чисел')
kolvo=int(input())
sum=0
for cikl in range(1,kolvo+1):
  sum += cikl**3
print('Сумма чисел = '+str(sum))  