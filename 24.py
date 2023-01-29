f = open('24.txt')
a = f.readline()
a = a.replace('D', ' ')
a = a.split()

maxx = 0
for i in range(len(a)):
    if i + 2 == len(a):
        break
    maxx = max(maxx, (len(a[i]) + len(a[i+1]) + len(a[i+2]) + 2))

print(maxx)