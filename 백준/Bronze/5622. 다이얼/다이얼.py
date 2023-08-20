dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()

time = 0

for i in dial:
    for j in i:
        for x in word:
            if j == x:
                time += dial.index(i)+3 # 숫자 1까지 2초, 인덱스는 0부터니까 +1      
print(time)