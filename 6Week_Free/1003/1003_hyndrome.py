# 분류: 6주차 자유주제
# 문제: 백준 1003 피보나치함수
# 문제 주소: https://www.acmicpc.net/problem/1003
# 푼 사람: 진홍엽
# 설명: DP

import sys
# def fibonacci(number):
#     if number == 0:
#         print(0)
#         return 0
#     elif number == 1:
#         print(1)
#         return 1
#     else:
#         return fibonacci(number-1) + fibonacci(number-2)

# dp를 위한 빈 배열, 0과 1 분리
ls_fibonacci_0 = [0] * 41
ls_fibonacci_1 = [0] * 41

# 0과 1의 출력 케이스를 함수로 분리 하여 n번째 피보나치 수를 재귀적으로 구함
# n-1 과 n 값을 이미 구한 경우, dp 빈 배열에서 값을 가져옴
def bi_fibonacci_0(number):
    if number == 0:
        return ls_fibonacci_0[0]
    elif number == 1:
        return ls_fibonacci_0[1]
    else:
        if ls_fibonacci_0[number - 1] != 0 and ls_fibonacci_0[number - 2] != 0:
            ls_fibonacci_0[number] = ls_fibonacci_0[number - 1] + ls_fibonacci_0[number - 2]
            
        else:
            ls_fibonacci_0[number] = bi_fibonacci_0(number-1) + bi_fibonacci_0(number-2)
    return ls_fibonacci_0[number]

def bi_fibonacci_1(number):
    if number == 0:
        return ls_fibonacci_1[0]
    elif number == 1:
        return ls_fibonacci_1[1]
    else:
        if ls_fibonacci_1[number - 1] != 0 and ls_fibonacci_1[number - 2] != 0:
            ls_fibonacci_1[number] = ls_fibonacci_1[number - 1] + ls_fibonacci_1[number - 2]
            
        else:
            ls_fibonacci_1[number] = bi_fibonacci_1(number-1) + bi_fibonacci_1(number-2)
    return ls_fibonacci_1[number]

i_t = int(sys.stdin.readline())

for i in range(i_t):
    i_n = int(sys.stdin.readline())
    print(bi_fibonacci_0(i_n), bi_fibonacci_1(i_n))
