# 분류: 4주차 그리디
# 문제: 백준 1541 잃어버린괄호
# 문제 주소: https://www.acmicpc.net/problem/1541
# 푼 사람: 진홍엽
# 설명: 그리디 수학 input처리

# 입력 받기
str_input = input()
# 숫자를 담을 리스트, 연산자의 수, 빼기 연산자의 수, 숫자를 담을 문자열 설정(0제거용)
ls_number = []
cnt_operator = 0
cnt_minus = 0
s_cnt = ''

for s_1 in str_input:
    # 연산자일 경우
    if (s_1 == '+') or (s_1 == '-'):
        cnt_operator += 1
        # 최초로 - 연산자가 나오는 위치 찾음
        if (s_1 == '-') and (cnt_minus ==0):
            cnt_minus = cnt_operator
        # 연산자는 숫자를 끊는 역할, 숫자 문자열 초기화
        ls_number.append(int(s_cnt))
        s_cnt = ''
    # 숫자를 받을 때 0으로 시작할 경우는 숫자로 받지 않음
    else:
        if s_cnt == '' and s_1 == '0':
            pass
        else:
            s_cnt += s_1
# 마지막 숫자는 연산자를 만나지 않으므로 for-else구문으로 처리
else:
    ls_number.append(int(s_cnt))
# - 연산자가 없을 경우 모든 숫자 합
sum_max = 0
if cnt_minus == 0:
    for i_1 in range(len(ls_number)):
        sum_max += ls_number[i_1]
# - 연산자가 있을 경우 최초 - 발견 위치부터 값을 뺌
else:
    for i_2 in range(cnt_minus):
        sum_max += ls_number[i_2]

    for i_3 in range(cnt_minus, len(ls_number)):
        sum_max -= ls_number[i_3]

print(sum_max)