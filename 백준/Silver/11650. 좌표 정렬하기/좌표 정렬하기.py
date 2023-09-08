arr=[]
n=int(input())

for i in range(n):
    x, y = map(int, input().split())
    arr.append((x,y))
    
arr.sort(key=lambda x: (x[0],x[1]))

for i in arr:
    x, y = i
    print(x, y)