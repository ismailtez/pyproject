game=input('если хотите поиграть введите - game ')
while game !="off":
    if game == "game":
        if game !='game':
            print('я такого не знаю')
    for i in range(0,3):
     k = int(input('угадай число от 1-5 '))
    if k == 5:
        print('вы выиграли билет на концерт')
        break
    game=input('если хотите поиграть введите - game ')
else:
    print('попробуй еще')
game=input('если хотите поиграть введите - game ')



