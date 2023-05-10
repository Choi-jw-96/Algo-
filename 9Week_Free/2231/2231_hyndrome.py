# 분류: 9주차 자유주제
# 문제: 백준 2231 분해합
# 문제 주소: https://www.acmicpc.net/problem/1931
# 푼 사람: 진홍엽
# 설명: 수학
# 평점: 2/5

# 분해합을 구하는 함수 정의
def divsum(input):
    sum = input
    while input >= 1:
        sum += input % 10
        input = input // 10
    return sum

s_n = input()
i_n = int(s_n)

i_generator = 0
# 분해합을 구하는 수의 범위 현재수 - 각 자리 개수 * 9 (각자리의 최대 수는 9)
for i in range(i_n - 9*len(s_n), i_n):
    if divsum(i) == i_n:
        i_generator = i
        break

if i_generator == 0:
    print(0)
else:
    print(i_generator)