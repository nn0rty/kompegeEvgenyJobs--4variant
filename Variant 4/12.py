for i1 in range(1,100):
    for i2 in range(1,100):
        for i3 in range(1,100):
            a = '0' + '1'*i1 + '2'*i2 + '3'*i3
            while ('01' in a) or ('02' in a) or ('03' in a):
                a = a.replace('01', '30', 1)
                a = a.replace('02', '3103', 1)
                a = a.replace('03', '1201', 1)
            if a.count('1') == 34 and a.count('2') == 24 and a.count('03') == 46:
                print(i3)