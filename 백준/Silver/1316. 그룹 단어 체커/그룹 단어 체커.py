# 단어의 개수
N = int(input())
group_word = N

for i in range(N) :
    word = input() # N개 입력 받기
    
    for j in range(len(word)-1) :
        # 연속된 글자는 continue
        if word[j] == word[j+1] :
            continue
        # 같은 글자가 아니면 -1
        elif word[j] in word[j+1:] :
            group_word -= 1
            break
print(group_word)