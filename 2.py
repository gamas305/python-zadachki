y = input('Введи число! :')
x = 5
try:
    if int(y)>x:
        print('Многа!')
    if int(y)<x:
        print('Мала!')
    elif int(y)==x:
        rint('Угадал!!!!!')
except:
    print('Ошибка!!!')