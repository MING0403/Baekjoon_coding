x, y, w, h = map(int, input().split())

# 직사각형의 경계선까지 가는 거리의 최소값
print(min(x, y, w-x, h-y))