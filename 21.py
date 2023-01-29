def F(x, p, m):
    if x >= 26:
        return p%2 == m%2
    if p == m:
        return False

    h = [F(x+1,p+1,m), F(x+2, p+1, m), F(x*2, p+1, m)]
    h1 = [F(x + 1, p + 1, m), F(x + 2, p + 1, m)]

    if x % 2 == 1:
        return any(h) if (p+1)%2 == m%2 else all(h)
    else:
        return any(h1) if (p + 1) % 2 == m % 2 else all(h1)

for s in range(1,26):
    for m in range(1,6):
        if F(s, 0, m):
            if m == 1 or m == 3 or m == 5:
                if m == 5:
                    print(s,m)
                break

