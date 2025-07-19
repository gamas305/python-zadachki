def silkom():
    inp = input("Введите число! :")
    sila = int(inp)
    if sila % 2 == 0 and sila > -1:
        print("Положительное чётное число!")
    elif sila % 2 != 0 and sila < -1:
        print("Отрицательное нечётное число!")
    else:
        print("Другое число!")
silkom()