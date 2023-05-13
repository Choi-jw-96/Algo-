# 분류: 10주차 정렬
# 문제: 백준 18310 안테나
# 문제 주소: https://www.acmicpc.net/problem 18310
# 푼 사람: 진홍엽
# 설명: 수학
# 평점: 2/5 가운데 점이 최소의 거리가 소요된다는 것은 조금 수학적인 접근법이지 않나...
i_n = int(input())
ls_house = list(map(int, input().split()))
ls_house.sort()
print(ls_house[(i_n - 1) // 2])