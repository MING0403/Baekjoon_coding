n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr_sort = sorted(arr)
print(arr_sort[-k])