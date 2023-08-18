N, X = map(int, input().split())
A = input().split()

# X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력
for i in range(N):
    if int(A[i]) < X:
        print(A[i], end=' ')