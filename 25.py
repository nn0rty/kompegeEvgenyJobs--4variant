import time
start_time = time.time()
def F(a):
    b = [10,12,14,16,18]
    pr = True
    for m in b:
        if a % m != 0:
            pr = False
    if pr == True:
        return a, a // max(b)

count = 0
for a in range(320401, 1000000):
    if F(a):
        if count <= 4:
            count += 1
            print(F(a))
        else:
            break