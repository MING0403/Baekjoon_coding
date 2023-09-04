arr = []
for i in range(5):
    num = int(input())
    arr.append(num)
arr.sort()

# 평균
print(int(sum(arr)/5))
# 중앙값
print(arr[2])