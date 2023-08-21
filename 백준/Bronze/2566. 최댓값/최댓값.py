# 9 X 9로 입력
a=[]
for i in range(9):
    row = list(map(int, input().split()))
    a.append(row)

# 기준 최댓값, 행 및 열 번호
max_num = 0
max_row, max_col = 0, 0

# 기준보다 크면 변경해라
for i in range(9):
    for j in range(9):
        if max_num <= a[i][j]:
            max_row = i+1
            max_col = j+1
            max_num = a[i][j]
            
print(max_num) # 최댓값
print(max_row, max_col) # 행번호, 열번호  