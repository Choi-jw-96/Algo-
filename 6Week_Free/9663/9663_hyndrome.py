# 분류: 6주차 자유주제
# 문제: 백준 9663 N-Queen
# 문제 주소: https://www.acmicpc.net/problem/9663
# 푼 사람: 진홍엽
# 설명: 백트래킹 재귀

# https://kjhoon0330.tistory.com/m/entry/BOJ-9663-N-Queen-Python
# https://aigong.tistory.com/474
# 시!간@!초!과!
i_n = int(input())
cnt_answer = 0
# 퀸은 한 행에 하나씩 밖에 존재할 수 없으므로 1차원 배열로 나타낼 수 있다.
row = [0] * i_n

# 유효 여부는 0 ~ r-1 까지만 확인한다. r부분부터 새롭게 놓을 것이기 때문
def is_valid(r):
    for i in range(r):
        # 세로 검사 대각선 검사
        if row[r] == row[i] or abs(r - i) == abs(row[r] - row[i]):
            return False
    return True


# r 행에 퀸 놓기
def put_queen(r):
    global cnt_answer
    # i_n개의 퀸을 모두 놓는데 성공했을 경우
    if r == i_n:
        cnt_answer += 1
        return
    
    # 가지치기 시작 백트래킹
    for i in range(i_n):
        row[r] = i
        # 해당 지점에 퀸을 놓는 것을 성공했을 경우 다음 행 퀸 놓기 가지치기 시작
        if is_valid(r):
            put_queen(r + 1)

put_queen(0)
print(cnt_answer)