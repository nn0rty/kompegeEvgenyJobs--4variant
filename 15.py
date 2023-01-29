def F(x, A):
    return ((x % 2 == 0) <= (not(x % 5 == 0))) or (x + A >= 90)

for A in range(1, 1000):
    pr = True
    for x in range(1, 1000):
        if F(x, A) == False:
            pr = False
    if pr == True:
        print(A)
        break