"""
Напишите программу печатающую скидку на поездку в зависимости от набранных баллов.
Программа должна запрашивать количество набранных баллов и печатать сообщение «Ваша скидка:» и скидку:
— от 0 до 49 баллов — «Скидка 10%»;
— от 50 до 99 баллов — «Скидка 15%»;
— от 100 баллов и выше — «Скидка 20%».
Примечание. Наличие функции является обязательным. Функция должна принимать количество набранных баллов.
"""
def sale(bal):
    if 0 <= bal < 50:
        print('Cкидка:', 'Скидка 10%')
    elif 49 < bal < 100:
        print('Cкидка:', 'Скидка 15%')
    elif 99 < bal:
        print('Cкидка:', 'Скидка 20%')


ball = int(input())
sale(ball)