# 분류: 10주차 정렬
# 문제: 백준 13164 행복유치원
# 문제 주소: https://www.acmicpc.net/problem 13164
# 푼 사람: 진홍엽
# 설명: 정렬 수학 최적화
# 평점: 3/5

# 키 차이가 최소로 하게 짜려면 겹치는 구간이 없게 조를 짜야함
# 조를 나누는 구간은 키 차이를 줄일 수 있는 구간
# 예시 1 3 5 6 10
# 전체 차이는 10 - 1 = 9
# 조를 1,3 / 5,6 / 10으로 나눌 경우
# 3와 5 사이인 2, 10과 6사이인 4 만큼이 전체 차이인 9에서 빠지게 된다
# 따라서 최소 비용은 9 -2 -4 = 3
i_n, i_k = map(int, input().split())
ls_height = list(map(int, input().split()))
ls_difference = [ls_height[i+1] - ls_height[i] for i in range(i_n-1)]
ls_difference.sort(reverse=True)
cost = ls_height[-1] - ls_height[0]
for i in range(i_k -1):
    cost -= ls_difference[i]
print(cost)