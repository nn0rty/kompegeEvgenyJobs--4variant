def F(x, y):
    if x > y or x == 60:
        return False
    if x == y:
        return True
    if x < y:
        return F(x + 5, y) + F(x * 5, y)

print(F(5,30)*F(30,280))