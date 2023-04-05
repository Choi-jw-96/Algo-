# 분류: 4주차 그리디
# 문제: 백준 13305 강의실배정
# 문제 주소: https://www.acmicpc.net/problem/13305
# 푼 사람: 진홍엽
# 설명: 그리디

i_n = int(input())
ls_distance = list(map(int,input().split()))
ls_price = list(map(int, input().split()))

# 1. 부분 성공
# 아래와 같이 풀이하게 될 경우 한칸 갈때마다 min을 돌리게 되어서 큰 리스트에 부적합
# cost_sum = 0
# for i_1 in range(len(ls_distance)):
#     cost_sum += ls_distance[i_1] * min(ls_price[:i_1 + 1])

# print(cost_sum)

# 반복문으로 한번만 순회
# 맨 뒤 도시의 기름 가격은 의미 없음
ls_price = ls_price[:-1]
price_lowest = 1000000000
distance_sum = 0
price_sum = 0
for i_1 in range(len(ls_price)):
    if ls_price[i_1] < price_lowest:
        price_sum += price_lowest * distance_sum
        price_lowest = ls_price[i_1]
        distance_sum = ls_distance[i_1]
    else:
        distance_sum += ls_distance[i_1]
else:
    price_sum += price_lowest * distance_sum
print(price_sum)