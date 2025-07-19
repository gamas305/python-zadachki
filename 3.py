inp = input('Введите число:')
inp2 = input('Введите второе число:')
try:
    chislo = int(inp)
    vtoroe = chislo*inp2
    print(vtoroe)
except:
    print('Пожалуйста, напишите число')