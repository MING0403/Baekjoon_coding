# 첫째 줄에 시험 본 과목의 개수 N
N = int(input())
# 세준이의 현재 성적
score = list(map(int, input().split()))
max_score = max(score)

# 점수/M*100 : 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점
slist=[]
for s in score:    # 새로운 점수 생성
    slist.append(s/max_score * 100)

# 새로운 평균
print(sum(slist)/N)