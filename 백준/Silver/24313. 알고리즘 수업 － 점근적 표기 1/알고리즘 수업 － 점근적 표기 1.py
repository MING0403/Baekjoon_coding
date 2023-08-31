# 첫째 줄에 함수 f(n)을 나타내는 정수 a1, a0가 주어진다.
a, b = map(int, input().split())
# 다음 줄에 양의 정수 c가 주어진다.
c = int(input())
# 다음 줄에 양의 정수 n0가 주어진다.
n = int(input())

if a*n+b<=c*n and c>=a:
    print(1)
else:
    print(0)