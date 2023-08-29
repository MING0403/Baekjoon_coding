cnt = 0
arr = []

a, b = map(int, input().split())

for i in range(1, a+1):
    if a%i == 0:
        arr.append(i)
    cnt += 1

# 약수가 아닐때 0, 맞을때는 인덱스 위치
if b>len(arr):
    print(0)
else:
    print(arr[b-1])