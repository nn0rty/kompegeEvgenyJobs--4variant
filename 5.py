for i in range(1,1000):
    N = bin(i)[2:]
    if int(N[-1]) % 2 == 0:
        N = '1' + N + '0'
    else:
        N = '11' + N + '10'
    b = 0
    for k in str(int(N, 2)):
        b += int(k)
    if b > 17:
        print(bin(b)[2:])
        break