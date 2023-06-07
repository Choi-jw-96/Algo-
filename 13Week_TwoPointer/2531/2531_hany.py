# 2531번 회전 초밥
'''
. 초밥의 종류를 번호로 표현할 때, 다음 그림은 회전 초밥 음식점의 벨트 상태의 예를 보여주고 있다.
벨트 위에는 같은 종류의 초밥이 둘 이상 있을 수 있다.

1. 벨트의 임의의 한 위치부터 k개의 접시를 연속해서 먹을 경우 할인된 정액 가격으로 제공한다.
2. 쿠폰에 적혀진 종류의 초밥 하나를 추가로 무료로 제공한다. 만약 이 번호에 적혀진 초밥이 현재 벨트 위에 없을 경우, 요리사가 새로 만들어 손님에게 제공한다.

회전 초밥 음식점의 벨트 상태, 메뉴에 있는 초밥의 가짓수, 연속해서 먹는 접시의 개수, 쿠폰 번호가 주어졌을 때,
손님이 먹을 수 있는 초밥 가짓수의 최댓값을 구하는 프로그램을 작성하시오.
'''
import sys
from collections import defaultdict
input = sys.stdin.readline

n, d, k, c = map(int, input().split()) # n: 접시수, d: 초밥가짓수, k:연속 먹는 접시 수, c: 쿠폰 번호
sushi = []
for _ in range(n):
    sushi.append(int(input()))
sushi.extend(sushi)

start = 0
end = 0
dict = defaultdict(int)
res = 0

dict[c] += 1

while end < k:
    dict[sushi[end]] += 1
    end += 1

while end < len(sushi):
    res = max(res, len(dict))

    dict[sushi[start]] -= 1
    if dict[sushi[start]] == 0:
        del dict[sushi[start]]
    dict[sushi[end]] += 1
    start += 1
    end += 1
print(res)