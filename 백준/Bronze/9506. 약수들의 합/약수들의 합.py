while True:
    n = int(input())
    if n==-1: # -1이 입력되면 종료
        break
    
    arr = []
    for i in range(1, n):
        if n%i==0:
            arr.append(i)
            
    if sum(arr) == n: # 동일하면 A+B+C로 출력
        print(n, " = ", " + ".join(str(i) for i in arr), sep="")
    else: # 만약 본인(n)을 제외한 약수의 값의 합이 동일하지 않다면
        print(n, "is NOT perfect.")