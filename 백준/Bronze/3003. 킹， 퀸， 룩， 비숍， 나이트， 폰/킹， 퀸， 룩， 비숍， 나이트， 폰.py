m_list = [1,1,2,2,2,8]
y = list(map(int,input().split()))
for i in range(len(m_list)):
    print(m_list[i] - y[i], end=" ")