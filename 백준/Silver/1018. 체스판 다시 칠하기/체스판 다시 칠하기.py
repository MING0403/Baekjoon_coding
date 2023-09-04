n, m = map(int, input().split())
board = []
result = []
 
for _ in range(n):
    board.append(input())
 
for i in range(n-7):
    for j in range(m-7):
        draw1 = 0
        draw2 = 0
 
        for a in range(i, i+8):
            for b in range(j, j+8):
                #  a + b를 2로 나눈 나머지가 0
                if (a + b) % 2 == 0:
                    # draw1은 검은색이 아닐 때 1을 더하여 색칠
                    if board[a][b] != 'B':
                        draw1 += 1
                    # draw2는 흰색이 아닐 때 1을 더하여 칠하는 것
                    if board[a][b] != 'W':
                        draw2 += 1
                else:
                    if board[a][b] != 'W':
                        draw1 += 1
                    if board[a][b] != 'B':
                        draw2 += 1
 
        result.append(draw1)
        result.append(draw2)
# 가장 적은 횟수를 출력
print(min(result))