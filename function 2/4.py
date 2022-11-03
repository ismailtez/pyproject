def cacluate(*a):
    s = sum(a)
    count = len(a)
    k = s / count
    return (k, [i for i in a if i > k])


print(cacluate(1, 2, 3, 4, 5))
