"""
Создайте функцию в демоне потока которая каждые 3 секунды будет писать "Вводите быстрее".
В основной части программы запросите ввод кода от бомбы и если код неверный выведите: "Вы взорвались", если верный - "Бомба разминирована"
"""
from threading import  Thread
import time
def qwerty():
    while True:
        time.sleep(3)

d = Thread(target=qwerty,daemon=True)
d.start()


code = 123456789
c = int(input('код'))
if c == code:
    print('код норм')
else:
    print('не норм')
