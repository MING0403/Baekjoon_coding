n = int(input())
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬
arr = []
for i in range(n):
    arr.append(int(input()))
arr_sort = sorted(arr)

# 결과를 한 줄에 하나씩 출력
for i in range(len(arr)):
    print(arr_sort[i])