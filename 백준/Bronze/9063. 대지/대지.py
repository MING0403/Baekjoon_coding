# 점의 개수
n=int(input())
x_lst = []
y_lst = []
for _ in range(n):
    x, y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)

result_x = max(x_lst) - min(x_lst)
result_y = max(y_lst) - min(y_lst)
print(result_x * result_y)