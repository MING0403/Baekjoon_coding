count = int(input())
num = input().split()
v = int(input())

c_sum = 0
# 입력된 정수 v가 몇 개인지
for i in range(count):
    if int(num[i]) == v:
        c_sum +=1
    else:
        c_sum += 0
        
print(c_sum)