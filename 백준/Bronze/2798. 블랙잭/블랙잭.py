# 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)
N, M = map(int, input().split())
# 카드에 쓰여 있는 수
arr = list(map(int, input().split()))

result = 0
# 카드의 합이 M을 넘으면 안됨
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if arr[i]+arr[j]+arr[k] > M:
                continue
            else:
                result = max(result, arr[i]+arr[j]+arr[k])
                
print(result)