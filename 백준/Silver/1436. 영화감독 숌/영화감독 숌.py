n = int(input())
first = 666
count = 0

while True:
    if '666' in str(first):   #1 n번째 수에 '666'이 포함되어 있다면
        count+=1               #2 카운트를 올려라
    if count == n:          #4 카운트랑 n번째 수가 같다면 
        print(first)           #5 nth를 출력
        break               #6 while문 종료
    first+=1                  #3 666이 포함된 수가 나올 때 까지 first를 1씩 증가