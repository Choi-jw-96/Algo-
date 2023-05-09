# 분류: 9주차 자유주제
# 문제: 백준 11723 분해합
# 문제 주소: https://www.acmicpc.net/problem/11723
# 푼 사람: 진홍엽
# 설명: set 구현
# 평점: 3/5

# set은 신기한 메소드가 많다
import sys

i_m = int(input())
set_cal = set()  
for i in range(i_m):
    ls_1 = sys.stdin.readline().split()
    if ls_1[0] == 'add':
        set_cal.add(int(ls_1[1]))
    elif ls_1[0] == 'remove':
        # if int(ls_1[1]) in set_cal:
        #     set_cal.remove(int(ls_1[1]))
        # set의 discard 매서드는 set 안에 해당 인자가 없어도 index error가 발생하지 않음
        set_cal.discard(int(ls_1[1]))
    elif ls_1[0] == 'check':
        if int(ls_1[1]) in set_cal:
            print(1)
        else:
            print(0)
    elif ls_1[0] == 'toggle':
        # set과 iterable한 객체를 비교해서 그 차이를 넣거나 빼주는 메서드, 반복 가능한 객체를 넣어야해서 리스트로 넣었음
        set_cal.symmetric_difference_update([int(ls_1[1])])
    elif ls_1[0] == 'all':
        set_cal = set(range(1, 21))
    else:
        set_cal.clear()