def Training():
    print("Чтобы узнать стоимость услуги введите 1.\n"
          "Чтобы узнать информацию о тренере введите 2.\n"
          "Чтобы узнать время работы зала введите 3.\n"
          "Чтобы узнать расписание тренера введите 4.\n")
    n = int(input("Введите номер от 1 до 4: "))
    if n == 1:
        return cost()
    elif n == 2:
        return trener()
    elif n == 3:
        return time()
    elif n == 4:
        return rasp()
    else:
        return 'Вводить можно только цифры от 1 до 4!'

def cost():
    return 'Цена составляет three hundred bucks.'
def trener():
    return 'Billy Harrington. Гений тренерства в Gachi стиле'
def time():
    return 'GYM доступен 24/7'
def rasp():
    return 'Расписание тренера: 60 секунд в минуту 60 минут в час 24 часа в сутки 7 дней в неделю 30 дней в месяц 12 месяцев в год и 100 лет в век.'
