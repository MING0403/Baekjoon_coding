# 영수증에 적힌 총 금액
t_price = int(input())
# 물건의 종류 수
type_count = int(input())

sum = 0 #계산한 금액
for _ in range(type_count):
    # 물건의 가격, 개수
    price, count = map(int, input().split())
    type_price = price * count # 물건 종류별 가격 구하기
    sum += type_price

if sum == t_price:
    print('Yes')
else:
    print('No')