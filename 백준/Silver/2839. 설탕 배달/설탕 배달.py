n = int(input()) #설탕

cnt = 0 #봉지수
while n>=0: #설탕이 남아있다면
    if n%5==0: #n이 5의 배수일 때와 0일때
        cnt += (n//5) # 5키로짜리 봉지
        print(cnt)
        break
    n -= 3 #5의 배수가 될 때까지 3킬로그램짜리 봉지에 담음
    cnt += 1
else:
    print(-1) #설탕이 음수가 될 경우 5,3kg 분류 불가