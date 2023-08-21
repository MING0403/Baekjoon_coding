a=[]
length = [] # 입력된 row 중 최대 개수
for i in range(5):
    row = input()
    a.append(row)
    length.append(len(row))

# 글자들을 공백없이 연속 출력
result = ''
for i in range(max(length)):
    for j in range(5):
        if i<length[j]:
            result += a[j][i] # 세로로 출력
            
print(result)