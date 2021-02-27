print('Введите количество чисел')
kolvo=int(input())
sum=0
for cikl in range(kolvo):
  chislo=int(input(str(cikl+1) +' е число: '))
  sum += chislo
print('Сумма чисел = '+str(sum))   