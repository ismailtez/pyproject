def cost(s):
    if 140 > s - 140 > 0:
        return 4.25
    elif s - 140 == 0:
        return 4
    else:
        s = s - 140
        return 0.25 + cost(s)


print(cost(int(input())))
