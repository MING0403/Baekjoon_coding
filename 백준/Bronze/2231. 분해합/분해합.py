N = int(input())
result= 0
# 분해 합
for i in range(1,N+1):
    num = list(map(int, str(i)))
    result = sum(num)+i
    # 분해합
    if result == N:
        print(i)
        break
    elif i == N:
        print(0)