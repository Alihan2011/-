from random import*
adolf = ['Adolf','Hitler', 'Germany', '1488', 'Mr.Beast']
a = ['камень','бумага','ножницы']

while True:
    sigmaa = int(input('Привет!\nвыбери одну из игр:\n1. Камень ножницы бумага\n2. рандомная буква\n3. угадать число\n4. закончить'))
    if sigmaa == 1:
        knb = int(input('1 - Ножницы;\n2 - Камень;\n3 - Бумага.'))
        bot = choice(a)
        if knb == 1: 
            print('Бот выйбрал', bot)
        elif knb == 2:
            print('Бот выйбрал', bot)
        elif knb == 3:
            print('Бот выйбрал', bot)
    elif sigmaa == 2:
        Hitler = choice(adolf)
        print(Hitler)
    elif sigmaa == 3:
        xyi = randint(1, 5)
        niger = int(input('Введите число от 1 до 5'))
        if niger == xyi:
            print('Вы выйграли')
        else: 
            print('Вы проиграли ')
    else:
        break