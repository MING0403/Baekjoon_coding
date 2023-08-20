T = int(input()) # 반복횟수

for _ in range(T):
    R, S = input().split() # S[#]에 대해서 R씩 반복
    for i in S:
        print(i*int(R), end="")
    print()