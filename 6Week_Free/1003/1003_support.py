def fibonacci(n) : 
    if n >= 3 :
        for i in range(2, n) :
            # 더해주면서 더한 수의 리스트를 차례대로 붙여넣는다
            fibonacci_0.append(fibonacci_0[i-1]+fibonacci_0[i])
            fibonacci_1.append(fibonacci_1[i-1]+fibonacci_1[i])
    # 제일 마지막 수 출력
    print(fibonacci_0[n],fibonacci_1[n])

T = int(input())

for t in range(T) :
    # 값을 받을때 마다 초기화
    fibonacci_0 = [1,0,1]
    fibonacci_1 = [0,1,1]
    n = int(input()) 
    fibonacci(n)