a=int(input('a='))
4
b=int(input('b='))
2
c=int(input('c='))
-8
d=b**2-4-a*c
print('Дискриминант='+str(d))
if d<0:
 print('Корней нет')
elif d==0:
 x=-b / (2 * a)
 print('x = ' + str(x))
else:
 x1 = (-b + d * 0.5) / (2 * a)
 x2 = (-b - d * 0.5) / (2 * a)
 print('x1 = ' + str(x1))
 print('x2 = ' + str(x2))
