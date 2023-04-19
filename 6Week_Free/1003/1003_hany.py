# 1003번 피보나치 함수
'''
int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n-1) + fibonacci(n-2);
    }
}
N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성
'''
# dp(n) = dp(n-1) + dp(n-2)
# dp(0) = 0
# dp(1) = 1
# 0과 1이 나올 떄마다 0과 1을 프린트한다.
# dp(2)부터 규칙 적용

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     cnt = [0, 0]

#     def fibonacci(n):
#         if n == 0:
#             cnt[0] += 1
#             return 0
#         elif n == 1:
#             cnt[1] += 1
#             return 1
#         else:
#             return fibonacci(n-2) + fibonacci(n-1)

#     fibonacci(n)
#     print(*cnt)

# 시간초과
# 다른 방식으로 풀어야 한다. 

t = int(input())

for _ in range(t):
    cnt0 = [1, 0]
    cnt1 = [0, 1]
    n = int(input())

    if n == 0:
        print(*cnt0)
    elif n == 1:
        print(*cnt1)
    else:
        for i in range(2, n + 1):
            cnt0.append(cnt0[i - 1] + cnt0[i - 2])
            cnt1.append(cnt1[i - 1] + cnt1[i - 2])
        print(f'{cnt0.pop()} {cnt1.pop()}')




## 구글링
# t = int(input())
# zero = [1, 0, 1]
# first = [0, 1, 1]

# def fibonacci(n):
#     if n >= len(zero):
#         for i in range(len(zero), n + 1):
#             zero.append(zero[i - 1] + zero[i - 2])
#             first.append(first[i - 1] + first[i - 2])
#     print(zero[n], first[n])

# for _ in range(t):
#     n = int(input())
#     fibonacci(n)