with open('17.txt') as f:
    a = [int(x) for x in f]

count = 0
maxx = 0
for i in range(len(a)):
    if i + 1 == len(a):
        break
    if a[i] % 117 == min(a) or a[i+1] % 117 == min(a):
        count += 1
        maxx = max(maxx, a[i+1] + a[i])
print(count, maxx)