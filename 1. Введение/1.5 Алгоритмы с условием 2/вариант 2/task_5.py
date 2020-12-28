a = int(input('Введите целое число a: '))
b = int(input('Введите целое число b: '))
c = int(input('Введите целое число c: '))

if(a > b):
  if a>c:
    print('Максимум = ', a)
  else:
    print('Максимум = ', c)
else:
  if b > c:
    print('Максимум = ', b)
  else:
    print('Максимум = ', c)
