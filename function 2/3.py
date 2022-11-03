def summ():
    a = input()
    if a == '':
        return 0.0
    else:
        return int(a) + summ()



print(summ())
