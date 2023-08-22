N = int(input())

for i in range(1,N):
    print(' '*(N-i)+'*'*(2*i-1))
# N부터 0까지 역순
for i in range(N,0,-1):
    print(' '*(N-i)+'*'*(2*i-1))