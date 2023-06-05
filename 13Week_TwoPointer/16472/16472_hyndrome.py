# 분류: 13주차 두포인터
# 문제: 백준 16472 고냥이
# 문제 주소: https://www.acmicpc.net/problem/16472
# 푼 사람: 진홍엽
# 설명: 두포인터 구현
# 평점: 3.5/5
i_n = int(input())
s_cat = input()
dct_s = {}
cnt_max = 0
cnt_current = 0
for i in range(len(s_cat)):
    # 딕셔너리에는 각 문자의 최근 index 값이 저장됨
    dct_s[s_cat[i]] = i
    # 딕셔너리의 키 종류가 인식할 수 있는 알파벳 종류 초과일 경우
    # print(dct_s)
    if len(dct_s) > i_n:
        # 딕셔너리의 value 값이 가장 작은 것은 key값을 삭제해야함
        s_remove = min(dct_s, key=dct_s.get)
        # 갱신된 문자열의 길이는 가장 오래된 문자가 제거된 이후 지점의 길이
        cnt_current  = i - dct_s[s_remove]
        # 길이 계산 이후 딕셔너리에서 해당 문자 제거
        dct_s.pop(s_remove)
        # print(dct_s)
        # print(cnt_current)
    # 딕셔너리의 키 종류가 인식할 수 있는 개수 이하일 경우 
    else:
        # cnt를 1 올려줌
        cnt_current += 1
        # print(dct_s)
        # print(cnt_current)
    # 최댓값 갱신 조건문 
    if cnt_current > cnt_max:
        cnt_max = cnt_current
        
print(cnt_max)