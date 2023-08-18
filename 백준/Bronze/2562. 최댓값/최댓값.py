total = []
for _ in range(9):
    total.append(int(input()))
    
print(max(total))    # 최댓값
print(total.index(max(total))+1) # 최댓값이 몇 번째 수인지
