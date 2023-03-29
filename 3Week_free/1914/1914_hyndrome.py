# 분류: 3주차 자유주제
# 문제: 백준 1914 하노이의탑
# 문제 주소: https://www.acmicpc.net/problem/1914
# 푼 사람: 진홍엽
# 설명: 재귀

# 정수 입력 받기
i_n = int(input())

# 이동을 저장할 리스트 형성
ls_stack = []

# hanoi(현재 쌓여있는 블록수, 시작지점, 종료지점)
# 하노이 탑 이동은 만약 높이가 5일 경우 아래 식처럼 나타낼 수 있음 (맨 아래의 블록을 종료지점으로 옮겨야한다는 것을 생각)
# hanoi(5, 1, 3) = hanoi(4, 1, 2) + hanoi(1, 1, 3,) + hanoi(4, 2, 3)

# 이동을 보여주는 함수 형성
def hanoi_stack(stack, start, end):
    # 블록이 1개일 경우 그대로 이동
    if stack == 1:
        ls_stack.append((start, end))
    else:
        # 시작지점과 종료지점이 아닌 지점을 left로 정의
        left = [i_1 for i_1 in [1, 2, 3] if (i_1 != start) and (i_1 != end)].pop()
        # 위에서 정리한 내용을 재귀
        hanoi_stack(stack - 1, start, left)
        hanoi_stack(1, start, end)
        hanoi_stack(stack - 1, left, end)

#  단순히 이동 횟수를 계산하는 함수를 정의
def hanoi_cnt(stack):
    if stack == 1:
        return 1
    else:
        return hanoi_cnt(1) + 2 * hanoi_cnt(stack - 1)

# 쌓여있는 블록이 20개 기준으로 함수를 선택
if i_n <= 20:
    hanoi_stack(i_n, 1, 3)
    print(len(ls_stack))
    for tup_1 in ls_stack:
        print(*tup_1)
else:
    cnt = 0
    cnt += hanoi_cnt(i_n)
    print(cnt)