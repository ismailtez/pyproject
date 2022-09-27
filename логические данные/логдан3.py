price = int(input('чек '))
if (int(price == '25')) or (int(price == '100')) or (int(price == '310')):
    print(int(price//2))
elif (int(price == '2500')) or (int(price == '400')) or (int(price == '50')):
    print(int(price//3))
else:
    print(price)
