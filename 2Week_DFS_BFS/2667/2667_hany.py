# 2667번 단지번호 붙이기
'''
집 있는 곳: 1
집 없는 곳: 0
집의 모임인 단지를 정의하고, 단지에 번호를 붙인다.
(단지 정의: 상하좌우에 다른 집이 있는 경우)
지도를 입력하여, 단지수를 출력 하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하는 프로그램을 작성하시오
'''

# 0. 입력 및 초기값 설정
from pprint import pprint
import sys
input = sys.stdin.readline

N = int(input())
group = [] # 전체 그래프

for _ in range(N):
    group.append(list(map(int, input().rstrip())))
# pprint(group)


# 1. dfs 함수 정의
def dfs(x, y, i):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if group[x][y] == 1:
        i.append('house') # 개별적인 단지를 세기 위함
        group[x][y] = 0
        dfs(x, y + 1, i)
        dfs(x, y - 1, i)
        dfs(x + 1, y, i)
        dfs(x - 1, y, i)
        return True
    return False

# 2. 값 도출
result = 0 # 총 단지 개수
house_num_lst = [] # 함수 인자 i에 해당함(단지 별 가구수를 구하기 위함)
calculation_lst = [] # 가구수 누적합 도출
fin_lst = [] # 최종 가구수 리스트

for x in range(N):
    for y in range(N):
        if dfs(x, y, house_num_lst) == True:
            result += 1
            calculation_lst.append(len(house_num_lst))
print(result)
# print(calculation_lst) -> [7, 15, 24]

for n in range(len(calculation_lst)):
    if calculation_lst[n] != calculation_lst[0]: # 그외의 값
        fin_lst.append(calculation_lst[n] - calculation_lst[n - 1])
    else: # 첫번째 값
        fin_lst.append(calculation_lst[n])

fin_lst.sort()
for _ in fin_lst:
    print(_)