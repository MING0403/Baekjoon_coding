a, b, c = map(int, input().split())

if a==b and b==c: # 모두 같은 눈이 나온 경우
    price = 10000+a*1000
elif a==b or b==c or a==c: # 같은 눈이 2개 나오는 경우
     if a==b or a==c:
        price = 1000+a*100
     elif b==c:
        price = 1000+b*100
else: # 모두 다른 눈이 나오는 경우
    price = max(a,b,c)*100
    
print(price)