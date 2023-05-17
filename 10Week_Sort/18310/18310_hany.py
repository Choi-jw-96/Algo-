# 18310번 안테나
'''
특정 위치의 집에 특별히 한 개의 안테나를 설치하기로 결정했다.
효율성을 위해 안테나로부터 모든 집까지의 거리의 총 합이 최소가 되도록 설치하려고 한다.
이 때 안테나는 집이 위치한 곳에만 설치할 수 있고, 논리적으로 동일한 위치에 여러 개의 집이 존재하는 것이 가능하다.
집들의 위치 값이 주어질 때, 안테나를 설치할 위치를 선택하는 프로그램을 작성하시오.

첫째 줄에 안테나를 설치할 위치의 값을 출력한다.
단, 안테나를 설치할 수 있는 위치 값으로 여러 개의 값이 도출될 경우 가장 작은 값을 출력한다.
'''
'''
중간값 구하면 됨
'''
import sys
input = sys.stdin.readline
n = int(input())
houses = sorted(list(map(int, input().split())))
print(houses[(n - 1) // 2])

# 시간초과
# import sys
# input = sys.stdin.readline
# n = int(input())
# houses = sorted(list(map(int, input().split())), reverse=True)
# antenna = 1e9
# res = 200000
# for standard in houses:
#     temp = 0
#     for house in houses:
#         temp += abs(standard - house)
#     if antenna >= temp:
#         antenna = temp
#         res = standard

# print(res)
