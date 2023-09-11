# 점 n개
n = int(input())

arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

# y좌표 증가순으로 정렬, x좌표 증가순으로 정렬
arr.sort(key = lambda x : (x[1], x[0]))

for data in arr:
    print(data[0], data[1])