M = int(input()) #최소
N = int(input()) #최대

arr=[]
for i in range(M, N+1):
    for j in range(2, i+1):
        if j==i:
            arr.append(i)
        if i%j==0: # 
            break
            
if not arr:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])