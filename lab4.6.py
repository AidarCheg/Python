print('Введите количество чисел')
kolvo=int(input())
sum=0
nesot = 0
for cikl in range(kolvo):
  chislo=int(input(str(cikl+1) +' е число: '))
  if chislo ==0:
    sum+=1
  else:
     nesot=0
if nesot != 0:
    print('НЕТ числа со значением 0')       
print('Количество чисел равных 0 = ' + str(sum))    