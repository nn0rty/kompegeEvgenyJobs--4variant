count = 0
for i1 in range(1,9):
    for i2 in range(9):
        for i3 in range(9):
            for i4 in range(9):
                for i5 in range(9):
                    s = f'{i1}{i2}{i3}{i4}{i5}'
                    if i1 % 2 == 0 and i5 != 1 and i5 != 8 and s.count('3') <= 1:
                        count += 1
print(count)