"""
Напишите программу принимающую ввод информации о треке(место в чарте,исполнитель, название) пока пользователь
не введет "off". Программа должна вывести всю информацию в виде словаря вида: {(место,испонитель): название трека}
"""
s = {}
while True:
    name = input('введите имя исполнителя: ')
    if name == 'off':
        break
    else:
        p = []
        p.append(name)
        place = input('введите место в чарте ')
        trek = input('трек ')
        p.append(place)
        p.append(trek)
        s[tuple(p[:2])] = p[2]
print(s)
