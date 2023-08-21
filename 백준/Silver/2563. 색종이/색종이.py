white = [[0 for j in range(100)] for i in range(100)]
counts = 0

N = int(input())

for i in range(N):
    x, y = list(map(int, input().split()))
    for xi in range(x, x+10):
        for yi in range(y, y+10):
            white[xi][yi] = 1

for j in white:
    counts += j.count(1)

print(counts)