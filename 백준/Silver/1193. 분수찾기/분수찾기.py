n = int(input())

line = 0
end = 0
while n > end:
    line += 1
    end += line

diff = end - n
# 대각선이 짝수
if line%2 == 0: 
    top = line - diff
    bottom = diff + 1
# 대각선이 홀수
else:
    top = diff + 1
    bottom = line - diff

print("%d/%d"%(top,bottom))