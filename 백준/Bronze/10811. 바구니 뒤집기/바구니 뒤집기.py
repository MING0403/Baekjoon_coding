N, M = map(int, input().split())
basket = [i for i in range(1,N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    result = basket[i-1:j]
    result.reverse() # 역순으로 바꾸기
    basket[i-1:j]=result

# 순서 바꾼 값 출력
for i in range(N):
    print(basket[i], end=' ')