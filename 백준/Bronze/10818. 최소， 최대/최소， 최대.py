N = int(input())
num = input().split()

# 최대/최소 기준 값
a = int(num[0])
b = int(num[0])

for i in range(N):
    if a < int(num[i]): # 기준값보다 크면
        a = int(num[i]) # 큰 값을 기준값으로 변경해라
    if b > int(num[i]): # 기준값보다 작으면
        b = int(num[i]) # 작은 값을 기준값으로 변경해라
        
print(b, a)