print('Введите количество чисел')
kolvo=int(input())
sum=1
for cikl in range(1,kolvo+1):
  sum *=cikl
  print(str(cikl) + '*'+ str(cikl+1),end=' ')
  print('Произведение чисел = '+str(sum))  