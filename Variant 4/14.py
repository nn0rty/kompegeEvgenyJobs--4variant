for x in range(1, 1000):
    a = 27 ** 7 - 3 ** 11 + 36 - x
    s = ''
    while a > 0:
        s = s + str(a % 3)
        a = a // 3
    b = 0
    for k in s:
        b += int(k)
    if b == 22:
        print(x)
        break