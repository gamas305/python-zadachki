def mem_memp():
    while True:
        inp = input("Введите число! :")
        try:
            mema = int(inp)
            break
        except ValueError:
            print("Это не число! Поробуй ещё раз!")
    if  mema < 12:
        print("Ты маленький!!")
    elif mema < 17:
        print("Ты подросток!")
    elif mema > 17 and mema < 60:
        print("Ты взрослый!")
    elif mema >= 60:
        print("Ты пенсионер!")

mem_memp()    