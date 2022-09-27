game = input('введите настольную игру ')
gameList = [game]
while (game !='0'):
    if (game not in gameList):
        print (game, 'игра добавлена в лист')
        if (game in gameList):
            print('такая игра уже есть')
        break

