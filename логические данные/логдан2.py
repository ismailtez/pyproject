time = int(input('сколько время? '))
money = int(input('сколько вышел чек? '))
if time == '10'or'11'or'12':
    print(int(money/2))
elif time == '20'or'21'or'22':
    print(int(money/4))
else:
    print(int(money))
