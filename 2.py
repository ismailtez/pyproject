"""
Создайте функцию напоминалку в отдельном потоке от основном программы.
Функция должна запрашивать о чем напомнить и через сколько секунд.
В основной части программы запустите поток с функцией и выполните задержку в 10 секунд.
После выполнения программа должна написать "программа завершается"
"""
from threading import Thread
import time
def napominalka():
    s = input('че напомнить')
    second = input('когда напомнить')


    time.sleep(int(second))
    print(s)

t1 = Thread(target=napominalka, name=None, args=())
t1.start()
t1.join()
time.sleep(10)
print('основной поток завершен')