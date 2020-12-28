num = int(input('Введите целое число: '))
ans = input('Перевести в байты - "b", в килобайты "k": ')

ans = ans.lower()
if ans == 'b':
    print('=', num * 1024)
elif ans == 'k':
    print('= ', num / 1024)
else:
    print('Неверный ввод')
