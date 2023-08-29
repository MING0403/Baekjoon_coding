# 올라갈 수 있는 높이 A
# 자는 동안 미끄러지는 높이 B
# 나무막대 높이 V
A, B, V = map(int, input().split())

day = (V-B)/(A-B)
print(int(day) if day == int(day) else int(day)+1)
